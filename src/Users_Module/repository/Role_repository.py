from typing import List
from fastapi import Depends
from database.db import get_db
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.dtos.update_user_dto import Update_User_DTO
from src.Users_Module.models.Role_entity import Role
from src.Users_Module.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.Users_Module.value_objects.Role_Type import Staff_Role_Type_Enum
from src.errors.Not_Found_Exception import NotFoundException
from sqlalchemy import exc


class RoleRepository:
    async def create_role_for_user(
        self,
        user_id: str,
        role: Staff_Role_Type_Enum,
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
