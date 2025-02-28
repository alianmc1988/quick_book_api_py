from typing import List
from fastapi import Depends
from database.db import get_db
from src.Business_Module.dtos.business_dtos.create_business_dto import Create_Business_DTO
from src.Business_Module.dtos.business_dtos.update_business_dto import Update_Business_DTO
from src.Business_Module.models.business_entity import Business


class Business_Repository:
        async def create_business(self, business_payload:Create_Business_DTO, db = Depends(get_db))->Business:
            business_to_create = business_payload.model_dump(exclude_none=True)
            business = Business(**business_to_create)
            db.add(business)
            await db.commit()
            await db.refresh(business)
            return business
           

        async def list_all_businesss_from_bar(self)-> List[Business]:
            pass


        async def get_business_by_id(self, business_id:str)-> Business:
            pass

        async def update_business(self,  business_id:str, business_payload:Update_Business_DTO)-> Business:
            pass

        async def delete_business(self, business_id:str)-> None:
            pass

def get_business_repository()->Business_Repository:
    return Business_Repository()