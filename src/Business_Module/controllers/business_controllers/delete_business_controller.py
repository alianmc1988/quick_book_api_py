from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.services.busines_usecases.delete_business_use_case import (
    Delete_Business_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Delete_Business_Controller(Base_Controller):
    def __init__(self, use_case: Delete_Business_Usecase, business_id: str):
        super().__init__(access_level=AccessLevel.SUDO)
        self.use_case = use_case
        self.business_id = business_id

    async def handle(self):
        return await self.use_case.execute(
            business_id=self.business_id, logged_user=self.logged_user
        )
