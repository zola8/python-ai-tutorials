import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home() -> str:
    return "It works!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# http://localhost:8080/
