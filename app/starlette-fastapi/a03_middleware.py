import logging

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Scope, Receive, Send

# https://dev.to/ceb10n/understanding-fastapi-how-starlette-works-43i1
# https://github.com/ceb10n/blog-posts/tree/master/understanding-fastapi-how-starlette-works

logger = logging.getLogger(__name__)


class LogRequestMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        logger.info(f"-> received a request at {scope['path']}")
        await self.app(scope, receive, send)


class LogResponseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        await self.app(scope, receive, send)
        logger.info("-> we are after the call; we responded...")


async def hello(request):
    logger.info("Great news, we got a request!")
    return PlainTextResponse("Hello, World!")


app = Starlette(
    routes=[
        Route('/', hello),
    ],
    middleware=[
        Middleware(LogRequestMiddleware),
        Middleware(LogResponseMiddleware)
    ]
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info('App started')
    uvicorn.run(app, host="0.0.0.0", port=8080)

# http://localhost:8080/
