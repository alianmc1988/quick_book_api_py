from src.Business_Module.dtos.business_dtos.create_business_dto import Create_Business_DTO
from src.Business_Module.dtos.business_dtos.update_business_dto import Update_Business_DTO


class Business_Repository:
        async def create_business(self, business_payload:Create_Business_DTO):
            pass

        async def list_all_businesss_from_bar(self):
            pass


        async def get_business_by_id(self, business_id:str):
            pass

        async def update_business(self,  business_id:str, business_payload:Update_Business_DTO):
            pass

        async def delete_business(self, business_id:str):
            pass