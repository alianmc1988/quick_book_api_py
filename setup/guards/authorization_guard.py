import logging
from typing import Annotated
from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import JSONResponse

# from jose import ExpiredSignatureError, JWTError
from fastapi.security import OAuth2PasswordBearer
import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.exc import SQLAlchemyError

from database.db import get_db
from database.db_error_handler import sqlAlchemy_error_handler
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import (
    UserRepository,
    get_user_repository,
)
from src.errors.Unauthorized_Exception import UnauthorizedException
from jwt.exceptions import ExpiredSignatureError
from configurations.config import settings
from sqlalchemy.ext.asyncio import AsyncSession


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token", scheme_name="JWT")


async def get_current_user(
    user_repository: UserRepository,
    db: AsyncSession,
    token: str,
) -> User:
    try:
        payload = jwt.decode(token, settings["JWT_SECRET_KEY"], algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise UnauthorizedException()
        user = await user_repository.get_user_by_id(user_id=user_id, db=db)
        if user is None:
            raise UnauthorizedException()
        return user

    except Exception as e:
        raise UnauthorizedException(detail=str(e))


user_dependency = Annotated[User, Depends(get_current_user)]


async def authorization_middleware(
    request: Request,
    token: str = Depends(oauth2_bearer),
    db: AsyncSession = Depends(get_db),
) -> None:
    userRepository = UserRepository()
    user = await get_current_user(
        token=token,
        user_repository=userRepository,
        db=db,
    )
    request.state.logged_user = user
    return user
