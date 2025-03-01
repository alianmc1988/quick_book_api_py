from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.services.space_usecases.update_space_use_case import (
    Update_Space_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Update_Space_Controller(Base_Controller):
    def __init__(self, use_case: Update_Space_Usecase):
        self.use_case = use_case

    async def handle(self, id: str, space_payload: Create_Space_DTO):
        return await self.use_case.execute(id, space_payload=space_payload)
