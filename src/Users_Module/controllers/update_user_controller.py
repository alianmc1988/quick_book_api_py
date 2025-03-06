from typing import Annotated
from fastapi import Depends

from src.Auth_Module.constants.access_levels import AccessLevel
from src.Users_Module.models.User_entity import User
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.dtos.update_user_dto import Update_User_DTO
from src.Users_Module.services.update_user_usecase import (
    Update_User_Usecase,
    get_update_user_use_case,
)


class Update_User_Controller(Base_Controller):
    def __init__(
        self, update_user_use_case: Update_User_Usecase, id: str, user: Update_User_DTO
    ):
        super().__init__(access_level=AccessLevel.GUEST)
        self.update_user_use_case = update_user_use_case
        self.id = id
        self.user = user

    async def define(self) -> User:
        return await self.update_user_use_case.execute(
            id=self.id, user=self.user, logged_user=self.logged_user.id
        )


def get_update_user_controller(
    update_user_use_case: Update_User_Usecase = Depends(get_update_user_use_case),
):
    return Update_User_Controller(update_user_use_case=update_user_use_case)


TypeUpdateUserController = Annotated[
    Update_User_Controller, Depends(get_update_user_controller)
]
