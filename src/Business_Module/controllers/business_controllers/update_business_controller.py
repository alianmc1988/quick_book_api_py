from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
from src.Business_Module.services.busines_usecases.update_business_use_case import (
    Update_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Update_Business_Controller(Base_Controller):
    def __init__(self, use_case: Update_Business_Usecase):
        self.use_case = use_case

    async def handle(self, id: str, business_payload: Update_Business_DTO):
        return await self.use_case.execute(
            business_id=id, business_payload=business_payload
        )
