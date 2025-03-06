from typing import Annotated
from fastapi import Depends
from src.Auth_Module.constants.access_levels import AccessLevel
from src.Users_Module.models.User_entity import User
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.dtos.create_user_dto import Create_User_DTO

from src.Users_Module.services.create_user_usecase import (
    Create_User_Usecase,
    get_create_user_use_case,
)


class Create_User_Controller(Base_Controller):
    def __init__(
        self, create_user_use_case: Create_User_Usecase, user_payload: Create_User_DTO
    ):
        super().__init__(access_level=AccessLevel.GUEST)
        self.create_user_use_case = create_user_use_case
        self.user_payload = user_payload

    async def handle(self) -> User:
        return await self.create_user_use_case.execute(user=self.user_payload)


def get_create_user_controller(
    create_user_use_case: Create_User_Usecase = Depends(get_create_user_use_case),
):
    return Create_User_Controller(create_user_use_case=create_user_use_case)


TypeCreateUserController = Annotated[
    Create_User_Controller, Depends(get_create_user_controller)
]
