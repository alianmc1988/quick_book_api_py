from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.services.space_usecases.create_space_use_case import (
    Create_Space_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Create_Space_Controller(Base_Controller):
    def __init__(self, use_case: Create_Space_Usecase, space_payload: Create_Space_DTO):
        super().__init__(access_level=AccessLevel.MANAGER)
        self.use_case = use_case
        self.space_payload = space_payload

    async def define(self):
        self.space_payload.set_business_id(business_id=self.ctx)
        response = await self.use_case.execute(space_payload=self.space_payload)
        return response
