from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, ExpiredSignatureError
from passlib.context import CryptContext

from database.db import get_db
from src.Auth_Module.dtos.auth_dto import Auth_DTO
from src.Auth_Module.dtos.auth_login_dto import AuthLogin_DTO
from src.Users_Module.dtos.user_dto import UserDTO
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors.Unauthorized_Exception import UnauthorizedException
from src.errors.messages.auth_error_messages import AuthErrorMessagesEnum
from configurations.config import settings
import jwt


auth_routes = APIRouter(prefix="/auth", tags=["Authentication API"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login", scheme_name="JWT")


@auth_routes.post(
    "/login",
    status_code=200,
    response_model=Auth_DTO,
)
async def login(
    login_payload: AuthLogin_DTO,
    db: AsyncSession = Depends(get_db),
    user_repository: UserRepository = Depends(),
):
    user = await authenticate_user_usecase(
        login_payload=login_payload, user_repo=user_repository, db=db
    )
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_payload: dict = {"id": str(user.id), "roles": user.roles}
    token = create_access_token(data=token_payload)
    response: Auth_DTO = Auth_DTO(access_token=token, token_type="bearer", user=user)
    return response


async def authenticate_user_usecase(
    login_payload: AuthLogin_DTO, user_repo: UserRepository, db: AsyncSession
):
    user = await user_repo.get_user_by_email(email=login_payload.email, db=db)
    if not user or not user.verify_password(login_payload.password):
        raise UnauthorizedException(detail=AuthErrorMessagesEnum.UNAUTHORIZED)

    return user


def create_access_token(data: dict):
    to_encode = {"sub": data["id"], "roles": data["roles"]}
    encoded_jwt = jwt.encode(to_encode, settings["JWT_SECRET_KEY"], algorithm="HS256")
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_bearer),
    user_repository: UserRepository = Depends(),
    db: AsyncSession = Depends(get_db),
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


@auth_routes.get("/me", status_code=200, response_model=UserDTO)
async def test(user: user_dependency):
    if not user:
        raise UnauthorizedException()
    return user
