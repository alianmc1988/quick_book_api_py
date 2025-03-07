from fastapi import Depends
from database.db import get_db
from src.Users_Module.models.Role_entity import Role
from sqlalchemy.ext.asyncio import AsyncSession


class RoleRepository:
    async def create_role_for_user(
        self,
        user_id: str,
        role: int,
        business_id: str,
        db: AsyncSession = Depends(get_db),
    ) -> Role:
        new_role = Role(user_id=user_id, role=role, business_id=business_id)
        db.add(new_role)
        await db.commit()
        await db.refresh(new_role)
        return new_role


async def get_role_repository():
    return RoleRepository()
