from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class CatchAllExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next)->Response:
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            return JSONResponse(
                status_code=500,
                content={"message": "Internal Server Error", "details": str(exc)},
            )
        

def global_exception_handler(app:FastAPI)->FastAPI:
    app.add_middleware(CatchAllExceptionMiddleware)
    return app