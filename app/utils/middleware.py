from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse


def handle_exception(request, exception):
    detail = (
        f"An error ocurred while processing {request.method} {request.url.path}."
        f"Please refer to customer support with Error Number"
    )
    return JSONResponse(status_code=500, content={"detail": detail})


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exception:
            return handle_exception(request, exception)
