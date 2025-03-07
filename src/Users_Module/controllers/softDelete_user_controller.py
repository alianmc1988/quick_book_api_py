from typing import Annotated
from fastapi import Depends

from src.Auth_Module.constants.access_levels import AccessLevel
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.services.softDelete_user_usecase import (
    SoftDelete_User_Usecase,
    get_softDelete_user_use_case,
)


class SoftDelete_User_Controller(Base_Controller):
    def __init__(self, softDelete_User_Usecase: SoftDelete_User_Usecase, id: str):
        super().__init__(access_level=AccessLevel.MANAGER)
        self.softDelete_User_Usecase = softDelete_User_Usecase
        self.id = id

    async def define(self) -> None:
        return await self.softDelete_User_Usecase.execute(
            id=self.id, logged_user=self.logged_user.id
        )


def get_softDelete_user_controller(
    softDelete_User_Usecase: SoftDelete_User_Usecase = Depends(
        get_softDelete_user_use_case
    ),
):
    return SoftDelete_User_Controller(softDelete_User_Usecase=softDelete_User_Usecase)


TypeCreateUserController = Annotated[
    SoftDelete_User_Controller, Depends(get_softDelete_user_controller)
]
