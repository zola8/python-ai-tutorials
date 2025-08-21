import uvicorn
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Router


async def homepage(request):
    return PlainTextResponse("Homepage")


async def about(request):
    return PlainTextResponse("About")


async def user(request):
    return PlainTextResponse(f"user: {request.path_params['user_id']}")


routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about),
    Route('/users/{user_id:int}', endpoint=user),
]

app = Router(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
