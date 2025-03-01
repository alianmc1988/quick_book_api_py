from src.Business_Module.services.busines_usecases.find_business_by_id_use_case import (
    Find_Business_By_Id_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Find_Business_ById_Controller(Base_Controller):
    def __init__(self, use_case: Find_Business_By_Id_Usecase):
        self.use_case = use_case

    async def handle(self, business_id: str):
        return await self.use_case.execute(business_id=business_id)
