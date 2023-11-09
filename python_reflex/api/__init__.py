import reflex as rx
from fastapi.responses import JSONResponse

__all__ = ["init_api"]


async def test_api() -> JSONResponse:
    return JSONResponse({"message": "Hello World"}, 200)


def init_api(app: rx.App):
    app.api.add_api_route("/test_api", test_api)
