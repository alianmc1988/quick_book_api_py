from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.services.busines_usecases.create_business_use_case import (
    Create_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Create_Business_Controller(Base_Controller):
    def __init__(self, use_case: Create_Business_Usecase):
        self.use_case = use_case

    async def handle(self, business_payload: Create_Business_DTO):
        return await self.use_case.execute(business_payload=business_payload)
