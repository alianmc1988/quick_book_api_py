from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.services.space_usecases.delete_space_use_case import (
    Delete_Space_Usecase,
)

from src.baseHandlers.Controller import Base_Controller


class Delete_Space_Controller(Base_Controller):
    def __init__(self, use_case: Delete_Space_Usecase, id: str):
        super().__init__(access_level=AccessLevel.SUPERVISOR)
        self.use_case = use_case
        self.id = id

    async def handle(self):
        result = await self.use_case.execute(
            id=self.id, logged_user=self.logged_user.id
        )
        return result
