from src.Business_Module.models.social_media_entity import Business_Social_Media
from src.Business_Module.models.space_entity import Space
from src.Business_Module.models.features_toggle import Business_feature_toggle

from src.Users_Module.models.Role_entity import Role
from src.Users_Module.models.User_entity import User
from typing import List
from fastapi import Depends
from sqlalchemy import select
from database.db import get_db
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
from src.Business_Module.models.business_entity import Business
from sqlalchemy.ext.asyncio import AsyncSession


from src.errors.Not_Found_Exception import NotFoundException
from src.helpers.io_helper import update_entity_data
from sqlalchemy.exc import SQLAlchemyError


class Business_Repository:
    async def create_business(
        self,
        business_payload: Create_Business_DTO,
        master_users: List[User],
        db: AsyncSession = Depends(get_db),
    ) -> Business:
        try:
            business_to_create = business_payload.model_dump(exclude_none=True)
            business = Business(**business_to_create)
            db.add(business)
            await db.flush()

            roles: List[Role] = []
            if master_users:
                for user in master_users:
                    roles.append(Role(business_id=business.id, user_id=user.id, role=0))
                db.add_all(roles)

            await db.commit()

            await db.refresh(business)
            return business

        except SQLAlchemyError as e:
            await db.rollback()
            raise e

    async def list_all_businesses(
        self, db: AsyncSession = Depends(get_db)
    ) -> List[Business]:
        result = await db.execute(
            select(Business).filter(Business.deleted_at.is_(None))
        )
        return result.scalars().all()

    async def get_business_by_id(
        self, business_id: str, db: AsyncSession = Depends(get_db)
    ) -> Business:
        result = await db.execute(
            select(Business)
            .filter(Business.deleted_at.is_(None))
            .where(Business.id == business_id)
        )
        business = result.scalars().first()
        if business is None:
            raise NotFoundException(detail=f"Business with id: {business_id} not found")
        return business

    async def get_business_by_id_with_delete(
        self, business_id: str, db: AsyncSession = Depends(get_db)
    ) -> Business:
        result = await db.execute(select(Business).where(Business.id == business_id))
        business = result.scalars().first()
        if business is None:
            raise NotFoundException(detail=f"Business with id: {business_id} not found")
        return business

    async def update_business(
        self,
        business_id: str,
        business_payload: Update_Business_DTO,
        logged_user: str,
        db: AsyncSession = Depends(get_db),
    ) -> Business:
        payload = business_payload.model_dump(exclude_none=True, exclude_unset=True)
        business = await self.get_business_by_id(business_id=business_id, db=db)
        updated_entity = update_entity_data(
            payload_obj=payload, entity_to_update=business, logged_user=logged_user
        )
        await db.commit()
        await db.refresh(updated_entity)
        return business

    async def delete_business(
        self, business_id: str, logged_user: str, db: AsyncSession = Depends(get_db)
    ) -> None:
        business = await self.get_business_by_id(business_id=business_id, db=db)
        business.soft_delete(logged_user=logged_user)
        await db.commit()
        await db.refresh(business)

    async def hard_delete_business(
        self, business_id: str, db: AsyncSession = Depends(get_db)
    ):
        business = await self.get_business_by_id_with_delete(
            business_id=business_id, db=db
        )
        await db.delete(business)
        await db.commit()


def get_business_repository() -> Business_Repository:
    return Business_Repository()
