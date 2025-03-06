from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.services.space_usecases.list_spaces_use_case import (
    List_Spaces_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class List_Spaces_Controller(Base_Controller):
    def __init__(self, use_case: List_Spaces_Usecase, business_id: str):
        super().__init__(access_level=AccessLevel.GUEST)
        self.use_case = use_case
        self.business_id = business_id

    async def define(self):
        return await self.use_case.execute(business_id=self.business_id)
