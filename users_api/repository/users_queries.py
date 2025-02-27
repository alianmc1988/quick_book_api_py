from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends

from database.db import get_db
from users_api.models.User_entity import User



async def list_users_query( db: AsyncSession = Depends(get_db))-> List[User]:
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_id_query(user_id: int, db: AsyncSession = Depends(get_db))->User:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()