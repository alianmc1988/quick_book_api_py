from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.services.space_usecases.find_space_byId_use_case import (
    Find_Space_ById_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Find_Space_ById_Controller(Base_Controller):
    def __init__(self, use_case: Find_Space_ById_Usecase, id: str):
        super().__init__(access_level=AccessLevel.GUEST)
        self.use_case = use_case
        self.id = id

    async def handle(self):
        result = await self.use_case.execute(space_id=self.id)
        return result
