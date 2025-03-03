from src.Business_Module.services.busines_usecases.delete_business_use_case import (
    Delete_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Delete_Business_Controller(Base_Controller):
    def __init__(self, use_case: Delete_Business_Usecase):
        self.use_case = use_case

    async def handle(self, business_id: str):
        return await self.use_case.execute(business_id=business_id)
