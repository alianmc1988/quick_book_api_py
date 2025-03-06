from typing import List

from fastapi import Depends
from sqlalchemy import select
from database.db import get_db
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO
from src.Business_Module.models.space_entity import Space
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors.Not_Found_Exception import NotFoundException
from src.helpers.io_helper import update_entity_data


class Space_Repository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_space(self, space_payload: Create_Space_DTO) -> Space:
        space_to_create = space_payload.model_dump()
        business = Space(**space_to_create)
        self.db.add(business)
        await self.db.commit()
        await self.db.refresh(business)
        return business

    async def list_all_spaces(self, active: bool = True) -> List[Space]:
        result = await self.db.execute(select(Space).filter(Space.deleted_at.is_(None)))
        return result.scalars().all()

    async def list_all_spaces_from_business(self, business_id: str) -> List[Space]:
        result = await self.db.execute(
            select(Space)
            .filter(Space.deleted_at.is_(None))
            .where(Space.business_id == business_id)
        )
        return result.scalars().all()

    async def find_space_by_id(self, space_id: str) -> Space:
        space_found = await self.db.execute(
            select(Space).filter(Space.deleted_at.is_(None)).where(Space.id == space_id)
        )
        result = space_found.scalars().first()
        if result is None:
            raise NotFoundException(detail=f"Business with id: {space_id} not found")
        return result

    async def find_space_by_id_with_deleted(self, id: str) -> Space:
        result = await self.db.execute(select(Space).where(Space.id == id))
        response = result.scalars().first()
        return response

    async def update_space(
        self, id: str, space_payload: Update_Space_DTO, logged_user: str
    ) -> Space:
        payload = space_payload.model_dump(
            exclude="business_id", exclude_unset=True, exclude_none=True
        )
        space = await self.find_space_by_id(space_id=id)
        updated_entity = update_entity_data(
            payload_obj=payload, entity_to_update=space, logged_user=logged_user
        )
        await self.db.commit()
        await self.db.refresh(updated_entity)
        return updated_entity

    async def delete_space(self, id: int, logged_user: str):
        space = await self.find_space_by_id_with_deleted(id)
        if space is None:
            raise ValueError(f"Space with id {id} not found")
        await self.db.delete(space)
        await self.db.commit()
        return {"message": "Space deleted successfully"}


def get_space_repository(db: AsyncSession = Depends(get_db)) -> Space_Repository:
    return Space_Repository(db=db)
