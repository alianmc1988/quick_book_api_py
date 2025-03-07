import logging
from typing import Annotated
from fastapi import Depends, Request

from fastapi.security import OAuth2PasswordBearer
import jwt


from database.db import get_db
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import (
    UserRepository,
)
from src.errors.Unauthorized_Exception import UnauthorizedException
from configurations.config import settings
from sqlalchemy.ext.asyncio import AsyncSession


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login", scheme_name="JWT")


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


async def authentication_middleware(
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

    #
