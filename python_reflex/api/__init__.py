import reflex as rx
from fastapi.responses import JSONResponse

__all__ = ["init_api"]


async def handle_request(api_route: str) -> JSONResponse:
    # TODO: Implement the ApiAtate to get the handler fbased on the url
    return JSONResponse({"message": "Hello World", "request_url": api_route}, 200)


def init_api(app: rx.App) -> None:
    app.api.add_api_route("/{api_route}", handle_request)
