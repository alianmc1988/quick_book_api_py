from fastapi import APIRouter, Depends, Request
from typing import List

from setup.guards.auth_guard import authentication_middleware
from src.Users_Module.controllers.create_role_controller import Create_Role_Controller
from src.Users_Module.controllers.create_user_controller import Create_User_Controller
from src.Users_Module.controllers.get_userById_controller import Get_UserById_Controller
from src.Users_Module.controllers.softDelete_user_controller import (
    SoftDelete_User_Controller,
)
from src.Users_Module.controllers.update_user_controller import Update_User_Controller
from src.Users_Module.dtos.create_role_dto import Create_Role_DTO
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.dtos.role_dto import Role_DTO
from src.Users_Module.dtos.update_user_dto import Update_User_DTO
from src.Users_Module.dtos.user_dto import UserDTO
from src.Users_Module.services.add_role_to_user_usecase import (
    Create_Role_Usecase,
    get_create_role_use_case,
)
from src.Users_Module.services.create_user_usecase import (
    get_create_user_use_case,
    Create_User_Usecase,
)
from src.Users_Module.services.get_user_byId_usecase import (
    Get_UserById_Usecase,
    get_userById_use_case,
)
from src.Users_Module.services.list_users_usecase import (
    get_list_users_use_case,
    List_Users_Usecase,
)
from src.Users_Module.controllers.list_users_controller import List_Users_Controller
from src.Users_Module.services.softDelete_user_usecase import (
    SoftDelete_User_Usecase,
    get_softDelete_user_use_case,
)
from src.Users_Module.services.update_user_usecase import (
    Update_User_Usecase,
    get_update_user_use_case,
)

user_routes = APIRouter(prefix="/user", tags=["Users API"])


@user_routes.post(
    "/",
    response_model=UserDTO,
    status_code=201,
)
async def create_user(
    user: Create_User_DTO,
    create_user_use_case: Create_User_Usecase = Depends(get_create_user_use_case),
):

    controller = Create_User_Controller(
        create_user_use_case=create_user_use_case, user_payload=user
    )
    return await controller.handle()


@user_routes.get(
    "/", dependencies=[Depends(authentication_middleware)], response_model=List[UserDTO]
)
async def list_users(
    request: Request,
    list_users_use_case: List_Users_Usecase = Depends(get_list_users_use_case),
):
    controller = List_Users_Controller(list_users_usecase=list_users_use_case)
    controller.access_control(request=request)
    return await controller.handle()


@user_routes.patch(
    "/{id}", dependencies=[Depends(authentication_middleware)], response_model=UserDTO
)
async def update_user(
    id: str,
    user: Update_User_DTO,
    request: Request,
    update_user_use_case: Update_User_Usecase = Depends(get_update_user_use_case),
):
    controller = Update_User_Controller(
        update_user_use_case=update_user_use_case, id=id, user=user
    )
    controller.access_control(request=request)
    return await controller.handle()


@user_routes.delete(
    "/{id}", dependencies=[Depends(authentication_middleware)], status_code=204
)
async def soft_delete_user(
    id: str,
    request: Request,
    softDelete_user_use_case: SoftDelete_User_Usecase = Depends(
        get_softDelete_user_use_case
    ),
):
    controller = SoftDelete_User_Controller(
        softDelete_User_Usecase=softDelete_user_use_case,
        id=id,
    )
    controller.access_control(request=request)
    return await controller.handle()


@user_routes.get(
    "/{id}", dependencies=[Depends(authentication_middleware)], response_model=UserDTO
)
async def get_user_by_id(
    id: str, get_UserById_Usecase: Get_UserById_Usecase = Depends(get_userById_use_case)
):
    controller = Get_UserById_Controller(
        get_UserById_Usecase=get_UserById_Usecase, id=id
    )
    return await controller.handle()


@user_routes.post(
    "/role",
    dependencies=[Depends(authentication_middleware)],
    response_model=Role_DTO,
    status_code=201,
)
async def create_role(
    role_payload: Create_Role_DTO,
    request: Request,
    create_role_use_case: Create_Role_Usecase = Depends(get_create_role_use_case),
):
    controller = Create_Role_Controller(
        create_role_use_case=create_role_use_case,
        role_payload=role_payload,
    )
    controller.access_control(request=request)
    return await controller.handle()
