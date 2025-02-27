from users_api.dtos.create_user_dto import Create_User_DTO
from users_api.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from fastapi import Depends
from typing_extensions import Callable

from users_api.repository.users_queries import get_user_by_id_query

CreateUserCommandType = Callable[[Create_User_DTO, AsyncSession], User]

async def create_user_command( user: Create_User_DTO, db: AsyncSession = Depends(get_db)) -> User:
    user_to_create = user.model_dump()
    user = User(**user_to_create)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def update_user_command( user_id: int, user_data: Create_User_DTO, db: AsyncSession = Depends(get_db)):
    user_to_update = user_data.model_dump() 
    user = await get_user_by_id_query(user_id, db)
    for key, value in user_to_update.items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user_command( user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id_query(user_id, db)
    db.delete(user)
    await db.commit()
    return user