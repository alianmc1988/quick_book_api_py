from fastapi import APIRouter, Depends
from typing import List

from users_api.controllers.create_user_controller import Create_User_Controller
from users_api.dtos.create_user_dto import Create_User_DTO
from users_api.dtos.user_dto import UserDTO
from users_api.services.create_user_usecase import get_create_user_use_case, Create_User_Usecase
from users_api.services.list_users_usecase import get_list_users_use_case, List_Users_Usecase
from users_api.controllers.list_users_controller import List_Users_Controller

user_routes = APIRouter(prefix="/users", tags=["Users API"])

@user_routes.post("/", response_model=UserDTO)
async def create_user(user: Create_User_DTO, create_user_use_case: Create_User_Usecase = Depends(get_create_user_use_case)):
    controller = Create_User_Controller(create_user_use_case=create_user_use_case)
    return await controller.handle(user)

@user_routes.get("/", response_model=List[UserDTO])
async def list_users(list_users_use_case: List_Users_Usecase = Depends(get_list_users_use_case)):
    controller = List_Users_Controller(list_users_usecase=list_users_use_case)
    return await controller.handle()