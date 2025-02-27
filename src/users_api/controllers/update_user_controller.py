from typing import Annotated
from fastapi import Depends

from src.baseHandlers.Controller import Base_Controller
from src.users_api.dtos.update_user_dto import Update_User_DTO
from src.users_api.services.update_user_usecase import Update_User_Usecase, get_update_user_use_case

class Update_User_Controller(Base_Controller):
    def __init__(self, update_user_use_case:Update_User_Usecase):
        self.update_user_use_case = update_user_use_case

    async def handle(self, id: str, user: Update_User_DTO):
        return await self.update_user_use_case.execute(id,user)
    

def get_update_user_controller(update_user_use_case: Update_User_Usecase = Depends(get_update_user_use_case)):
    return Update_User_Controller(update_user_use_case=update_user_use_case)

TypeUpdateUserController = Annotated[Update_User_Controller, Depends(get_update_user_controller)]

   