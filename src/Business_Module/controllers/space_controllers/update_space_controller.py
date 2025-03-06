from src.Auth_Module.constants.access_levels import AccessLevel
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO
from src.Business_Module.services.space_usecases.update_space_use_case import (
    Update_Space_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Update_Space_Controller(Base_Controller):
    def __init__(
        self, use_case: Update_Space_Usecase, id: str, space_payload: Update_Space_DTO
    ):
        super().__init__(access_level=AccessLevel.SUPERVISOR)
        self.use_case = use_case
        self.id = id
        self.space_payload = space_payload

    async def define(self):
        return await self.use_case.execute(
            id=self.id,
            space_payload=self.space_payload,
            logged_user=self.logged_user.id,
        )
