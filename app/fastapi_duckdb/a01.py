import duckdb
import uvicorn
from fastapi import FastAPI

from data_types import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=Item | None)
def read_item(item_id: str) -> Item | None:
    rows = conn.execute(f"SELECT * FROM items WHERE id = {item_id}").fetchall()
    return None if len(rows) == 0 \
        else [Item(id=row[0], name=row[1], description=row[2], price=row[3]) for row in rows][0]


@app.get("/items/", response_model=list[Item])
def list_items() -> list[Item]:
    rows = conn.execute("SELECT * FROM items").fetchall()
    return [Item(id=row[0], name=row[1], description=row[2], price=row[3]) for row in rows]
    # similar to JDBC


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    # Initialize in-memory DuckDB
    conn = duckdb.connect(':memory:')
    conn.execute("CREATE TABLE items AS FROM 'example.csv';")

    uvicorn.run(app, host="0.0.0.0", port=8080)

# http://localhost:8080/
# http://localhost:8080/redoc
