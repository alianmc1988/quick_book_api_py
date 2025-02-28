from typing import List
from fastapi import Depends
from sqlalchemy import select
from database.db import get_db
from src.Business_Module.dtos.business_dtos.create_business_dto import Create_Business_DTO
from src.Business_Module.dtos.business_dtos.update_business_dto import Update_Business_DTO
from src.Business_Module.models.business_entity import Business
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc


from src.Business_Module.models.social_media_entity import Business_Social_Media
from src.Business_Module.models.space_entity import Space
from src.Users_Module.models.Role_entity import Role
from src.Users_Module.models.User_entity import User
from src.errors.Not_Found_Exception import NotFoundException
from src.helpers.io_helper import update_object_entity


class Business_Repository:
        async def create_business(self, business_payload:Create_Business_DTO, db:AsyncSession = Depends(get_db))->Business:
            business_to_create = business_payload.model_dump(exclude_none=True)
            business = Business(**business_to_create)
            db.add(business)
            await db.commit()
            await db.refresh(business)
            return business
           

        async def list_all_businesses(self, db:AsyncSession = Depends(get_db))-> List[Business]:
            result = await db.execute(select(Business).filter(Business.deleted_at.is_(None)))
            return result.scalars().all()


        async def get_business_by_id(self, business_id:str, db:AsyncSession = Depends(get_db))-> Business:
            result = await db.execute(select(Business).filter(Business.deleted_at.is_(None)).where(Business.id == business_id))
            business = result.scalars().first()
            if business is None:
                raise NotFoundException(detail=f'Business with id: {business_id} not found')
            return business

        async def update_business(self,  business_id:str, business_payload:Update_Business_DTO, db:AsyncSession = Depends(get_db))-> Business:
            payload = business_payload.model_dump(exclude_none=True, exclude_unset=True)
            business = await self.get_business_by_id(business_id=business_id, db=db)
            updated_entity = update_object_entity(payload_obj=payload, entity_to_update=business)
            await db.commit()
            await db.refresh(updated_entity)
            return business
            

        async def delete_business(self, business_id:str, db:AsyncSession = Depends(get_db))-> None:
            pass

def get_business_repository()->Business_Repository:
    return Business_Repository()