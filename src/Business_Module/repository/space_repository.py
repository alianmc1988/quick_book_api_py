from typing import List

from fastapi import Depends
from database.db import get_db
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO
from src.Business_Module.models.space_entity import Space
from sqlalchemy.ext.asyncio import AsyncSession



class Space_Repository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_space(self, space_payload:Create_Space_DTO)->Space:
        space_to_create = space_payload.model_dump()
        business = Space(**space_to_create)
        self.db.add(business)
        await self.db.commit()
        await self.db.refresh(business)
        return business

    async def list_all_spaces_from_bar(self, business_id:str)->List[Space]:
        pass

    async def list_active_spaces_from_bar(self, business_id:str)->List[Space]:
        pass

    async def get_space_by_id(self, business_id:str, space_id:str)->Space:
        pass

    async def update_space(self,  business_id:str, space_payload:Update_Space_DTO)->Space:
        pass

    async def delete_space(self, business_id:str, space_id:str)->None:
        pass

def get_space_repository(db: AsyncSession = Depends(get_db))->Space_Repository:
    return Space_Repository(db=db)