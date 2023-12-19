from fastapi.responses import JSONResponse


def handler() -> JSONResponse:
    return JSONResponse({"message": "Hello World"}, 200)
