from typing import List
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO
from src.Business_Module.models.space_entity import Space


class Space_Repository:
    async def create_spot(self, spot:Create_Space_DTO)->Space:
        pass

    async def list_all_spots_from_bar(self, business_id:str)->List[Space]:
        pass

    async def list_active_spots_from_bar(self, business_id:str)->List[Space]:
        pass

    async def get_spot_by_id(self, business_id:str, spot_id:str)->Space:
        pass

    async def update_spot(self,  business_id:str, spot_payload:Update_Space_DTO)->Space:
        pass

    async def delete_spot(self, business_id:str, spot_id:str)->None:
        pass