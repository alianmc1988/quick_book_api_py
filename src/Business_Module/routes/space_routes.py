from typing import List
from fastapi import APIRouter, Depends, Request


from src.Business_Module.controllers.space_controllers.create_space_controller import (
    Create_Space_Controller,
)
from src.Business_Module.controllers.space_controllers.delete_space_controller import (
    Delete_Space_Controller,
)
from src.Business_Module.controllers.space_controllers.find_space_byId_controller import (
    Find_Space_ById_Controller,
)
from src.Business_Module.controllers.space_controllers.list_spaces_controller import (
    List_Spaces_Controller,
)
from src.Business_Module.controllers.space_controllers.update_space_controller import (
    Update_Space_Controller,
)


from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.space_dto import Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO


from src.Business_Module.services.space_usecases.create_space_use_case import (
    Create_Space_Usecase,
    get_create_space_usecase,
)
from src.Business_Module.services.space_usecases.delete_space_use_case import (
    Delete_Space_Usecase,
    get_delete_space_usecase,
)
from src.Business_Module.services.space_usecases.find_space_byId_use_case import (
    Find_Space_ById_Usecase,
    get_find_space_byId_usecase,
)
from src.Business_Module.services.space_usecases.list_spaces_use_case import (
    List_Spaces_Usecase,
    get_list_spaces_usecase,
)
from src.Business_Module.services.space_usecases.update_space_use_case import (
    Update_Space_Usecase,
    get_update_space_usecase,
)


space_routes = APIRouter(prefix="/space")


@space_routes.post("/", response_model=Space_DTO, status_code=201)
async def create_space(
    space_payload: Create_Space_DTO,
    request: Request,
    create_space_use_case: Create_Space_Usecase = Depends(get_create_space_usecase),
):
    controller = Create_Space_Controller(
        use_case=create_space_use_case, space_payload=space_payload
    )
    controller.access_control(request=request)
    return await controller.handle()


@space_routes.get("/", response_model=List[Space_DTO], status_code=200)
async def list_spaces(
    business_id: str,
    request: Request,
    list_spaces_use_case: List_Spaces_Usecase = Depends(get_list_spaces_usecase),
):
    controller = List_Spaces_Controller(
        use_case=list_spaces_use_case, business_id=business_id
    )
    controller.access_control(request=request)
    return await controller.handle()


@space_routes.get("/{id}", response_model=Space_DTO, status_code=200)
async def find_space_by_id(
    id: str,
    request: Request,
    find_space_byId_use_case: Find_Space_ById_Usecase = Depends(
        get_find_space_byId_usecase
    ),
):
    controller = Find_Space_ById_Controller(use_case=find_space_byId_use_case, id=id)
    controller.access_control(request=request)
    return await controller.handle()


@space_routes.patch("/{id}", response_model=Space_DTO, status_code=201)
async def update_space(
    request: Request,
    id: str,
    space_payload: Update_Space_DTO,
    update_space_use_case: Update_Space_Usecase = Depends(get_update_space_usecase),
):
    controller = Update_Space_Controller(
        use_case=update_space_use_case, id=id, space_payload=space_payload
    )
    controller.access_control(request=request)
    return await controller.handle()


@space_routes.delete("/{id}", status_code=204)
async def delete_space(
    id: str,
    request: Request,
    delete_space_usecase: Delete_Space_Usecase = Depends(get_delete_space_usecase),
):
    controller = Delete_Space_Controller(use_case=delete_space_usecase, id=id)
    controller.access_control(request=request)
    return await controller.handle()
