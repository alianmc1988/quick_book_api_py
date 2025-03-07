import logging
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

DB_Error_Constants: dict[str, str] = {
    "gkpj": "The Entity already exists for the current context"
}


def sqlAlchemy_error_handler(e: SQLAlchemyError, logger: logging.Logger):
    try:
        message = DB_Error_Constants[e.code]
        logger.error(f"{__name__}: {message}")
        if message is not None:
            return JSONResponse(
                status_code=422,
                content={"message": message},
            )
    except Exception as e:
        raise e
