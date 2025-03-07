import logging
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.exc import SQLAlchemyError

from database.db_error_handler import sqlAlchemy_error_handler


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class CatchAllExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
            return response
        except SQLAlchemyError as e:
            return sqlAlchemy_error_handler(e, logger=logger)
        except Exception as exc:

            print(type(exc))
            logger.error(f"Unhandled error: {str(exc)}")
            return JSONResponse(
                status_code=500,
                content={"message": "Internal Server Error", "details": str(exc)},
            )


def global_exception_handler(app: FastAPI) -> FastAPI:
    app.add_middleware(CatchAllExceptionMiddleware)
    return app
