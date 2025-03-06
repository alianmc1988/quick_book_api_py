from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.services.busines_usecases.create_business_use_case import (
    Create_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Create_Business_Controller(Base_Controller):
    def __init__(
        self, use_case: Create_Business_Usecase, business_payload: Create_Business_DTO
    ):
        super().__init__(access_level=AccessLevel.SUDO)
        self.business_payload = business_payload
        self.use_case = use_case

    async def define(self):
        return await self.use_case.execute(business_payload=self.business_payload)
