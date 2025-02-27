from src.Business_Module.dtos.spot_dtos.create_spot_dto import Create_Spot_DTO
from src.Business_Module.dtos.spot_dtos.update_spot_dto import Update_Spot_DTO


class Space_Repository:
    async def create_spot(self, spot:Create_Spot_DTO):
        pass

    async def list_all_spots_from_bar(self, business_id:str):
        pass

    async def list_active_spots_from_bar(self, business_id:str):
        pass

    async def get_spot_by_id(self, business_id:str, spot_id:str):
        pass

    async def update_spot(self,  business_id:str, spot_payload:Update_Spot_DTO):
        pass

    async def delete_spot(self, business_id:str, spot_id:str):
        pass