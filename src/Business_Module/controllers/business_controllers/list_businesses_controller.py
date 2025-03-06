from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.services.busines_usecases.list_businesses_use_case import (
    List_Businesses_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class List_Businesses_Controller(Base_Controller):
    def __init__(self, use_case: List_Businesses_Usecase):
        super().__init__(access_level=AccessLevel.SUDO)
        self.use_case = use_case

    async def define(self):
        return await self.use_case.execute()
