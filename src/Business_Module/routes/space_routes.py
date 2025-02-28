from typing import List
from fastapi import APIRouter, Depends

from src.Business_Module.controllers.business_controllers.create_business_controller import (
    Create_Business_Controller,
)
from src.Business_Module.controllers.business_controllers.delete_business_controller import (
    Delete_Business_Controller,
)
from src.Business_Module.controllers.business_controllers.find_business_byId_controller import (
    Find_Business_ById_Controller,
)
from src.Business_Module.controllers.business_controllers.list_businesses_controller import (
    List_Businesses_Controller,
)
from src.Business_Module.controllers.business_controllers.update_business_controller import (
    Update_Business_Controller,
)
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
from src.Business_Module.dtos.business_dtos.business_dto import Business_DTO
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.dtos.space_dtos.space_dto import Space_DTO
from src.Business_Module.dtos.space_dtos.update_space_dto import Update_Space_DTO
from src.Business_Module.services.busines_usecases.create_business_use_case import (
    Create_Business_Usecase,
    get_create_business_usecase,
)
from src.Business_Module.services.busines_usecases.delete_business_use_case import (
    Delete_Business_Usecase,
    delete_business_usecase,
)
from src.Business_Module.services.busines_usecases.find_business_by_id_use_case import (
    Find_Business_By_Id_Usecase,
    find_business_by_id_usecase,
)
from src.Business_Module.services.busines_usecases.list_businesses_use_case import (
    List_Businesses_Usecase,
    get_list_businesses_usecase,
)
from src.Business_Module.services.busines_usecases.update_business_use_case import (
    Update_Business_Usecase,
    update_business_usecase,
)
from src.Business_Module.services.space_usecases import find_space_byId_use_case
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
    create_space_use_case: Create_Space_Usecase = Depends(get_create_space_usecase),
):
    controller = Create_Space_Controller(use_case=create_space_use_case)
    return await controller.handle(space_payload=space_payload)


@space_routes.get("/", response_model=List[Space_DTO], status_code=200)
async def list_spaces(
    business_id: str,
    list_spaces_use_case: List_Spaces_Usecase = Depends(get_list_spaces_usecase),
):
    controller = List_Spaces_Controller(use_case=list_spaces_use_case)
    return await controller.handle(business_id=business_id)


@space_routes.get("/{id}", response_model=Space_DTO, status_code=200)
async def find_space_by_id(
    id: str,
    find_space_byId_use_case: Find_Space_ById_Usecase = Depends(
        get_find_space_byId_usecase
    ),
):
    controller = Find_Space_ById_Controller(use_case=find_space_byId_use_case)
    return await controller.handle(id=id)


@space_routes.patch("/{id}", response_model=Space_DTO, status_code=201)
async def update_space(
    id: str,
    space_payload: Update_Space_DTO,
    update_space_use_case: Update_Space_Usecase = Depends(get_update_space_usecase),
):
    controller = Update_Space_Controller(use_case=update_space_use_case)
    return await controller.handle(id=id, space_payload=space_payload)


@space_routes.delete("/{id}", status_code=204)
async def delete_space(
    id: str,
    delete_space_usecase: Delete_Space_Usecase = Depends(get_delete_space_usecase),
):
    controller = Delete_Space_Controller(use_case=delete_space_usecase)
    return await controller.handle(id=id)
