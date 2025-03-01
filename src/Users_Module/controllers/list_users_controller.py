from typing import List
from fastapi import Depends, HTTPException

from src.Users_Module.models.User_entity import User
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.services.list_users_usecase import (
    get_list_users_use_case,
    List_Users_Usecase,
)


class List_Users_Controller(Base_Controller):
    def __init__(self, list_users_usecase: List_Users_Usecase):
        self.list_users_usecase = list_users_usecase

    async def handle(self) -> List[User]:
        try:
            return await self.list_users_usecase.execute()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


def get_list_users_controller(
    list_users_use_case: List_Users_Usecase = Depends(get_list_users_use_case),
):
    return List_Users_Controller(list_users_usecase=list_users_use_case)
