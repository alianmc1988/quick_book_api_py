from fastapi import Depends
from database.db import get_db
from users_api.dtos.create_user_dto import Create_User_DTO
from users_api.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from bcrypt import hashpw, gensalt


class UserRepository:

    async def create_user(self, user: Create_User_DTO, db: AsyncSession = Depends(get_db)):
        user_to_create = user.model_dump()
        user = User(**user_to_create)
        user.hash_password()
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    
    async def list_users(self, db: AsyncSession = Depends(get_db)):
        result = await db.execute(select(User))
        return result.scalars().all()
    
    async def get_user_by_id(self, user_id: int, db: AsyncSession = Depends(get_db)):
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()
    
    async def update_user(self, user_id: int, user_data: Create_User_DTO, db: AsyncSession = Depends(get_db)):
        user_to_update = user_data.model_dump() 
        user = await self.get_user_by_id(user_id, db)
        for key, value in user_to_update.items():
            if key == 'password':
                value = hashpw(value.encode('utf-8'), gensalt())
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user
    
    async def delete_user(self, user_id: int, db: AsyncSession = Depends(get_db)):
        user = await self.get_user_by_id(user_id, db)
        db.delete(user)
        await db.commit()
        return user
    







    
async def get_user_repository():
    return UserRepository()

