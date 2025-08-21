import uvicorn


class SimplestFrameworkEver:
    async def __call__(self, scope, receive, send):
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],

        })
        await send({
            "type": "http.response.body",
            "body": b"Hello, World!",
        })


if __name__ == "__main__":
    app = SimplestFrameworkEver()
    uvicorn.run(app, host="0.0.0.0", port=8080)

# http://localhost:8080/
