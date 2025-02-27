from typing import Annotated
from fastapi import Depends
from src.baseHandlers.Controller import Base_Controller
from src.users_api.dtos.create_user_dto import Create_User_DTO

from src.users_api.services.create_user_usecase import Create_User_Usecase, get_create_user_use_case

class Create_User_Controller(Base_Controller):
    def __init__(self, create_user_use_case:Create_User_Usecase):
        self.create_user_use_case = create_user_use_case

    async def handle(self, user: Create_User_DTO):
        return await self.create_user_use_case.execute(user)
    

def get_create_user_controller(create_user_use_case:Create_User_Usecase = Depends(get_create_user_use_case)):
    return Create_User_Controller(create_user_use_case=create_user_use_case)

TypeCreateUserController = Annotated[Create_User_Controller, Depends(get_create_user_controller)]

   