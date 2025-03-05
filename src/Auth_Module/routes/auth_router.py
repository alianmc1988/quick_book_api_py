from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from database.db import get_db


auth_routes = APIRouter(prefix="/auth", tags=["Authentication API"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


@auth_routes.post("/login", status_code=201, db=Depends(get_db))
async def login():
    pass
