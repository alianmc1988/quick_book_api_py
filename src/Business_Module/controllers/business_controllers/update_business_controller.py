from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
from src.Business_Module.services.busines_usecases.update_business_use_case import (
    Update_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Update_Business_Controller(Base_Controller):
    def __init__(
        self,
        use_case: Update_Business_Usecase,
        business_payload: Update_Business_DTO,
        id: str,
    ):
        super().__init__(access_level=AccessLevel.OWNER)
        self.use_case = use_case
        self.business_payload = business_payload
        self.id = id

    async def define(self):
        return await self.use_case.execute(
            business_id=self.id,
            business_payload=self.business_payload,
            logged_user=self.logged_user,
        )
