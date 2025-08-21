import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def hello(request):
    return PlainTextResponse("Hello, World!")


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/hello', hello),
])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# http://localhost:8080/
