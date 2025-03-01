from typing import Annotated
from fastapi import Depends

from src.Users_Module.models.User_entity import User
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.services.get_user_byId_usecase import (
    Get_UserById_Usecase,
    get_userById_use_case,
)


class Get_UserById_Controller(Base_Controller):
    def __init__(self, get_UserById_Usecase: Get_UserById_Usecase):
        self.get_UserById_Usecase = get_UserById_Usecase

    async def handle(self, id: str) -> User:
        return await self.get_UserById_Usecase.execute(id)


def get_userById_controller(
    get_UserById_Usecase: Get_UserById_Usecase = Depends(get_userById_use_case),
):
    return Get_UserById_Controller(get_UserById_Usecase=get_UserById_Usecase)


TypeCreateUserController = Annotated[
    Get_UserById_Controller, Depends(get_userById_controller)
]
