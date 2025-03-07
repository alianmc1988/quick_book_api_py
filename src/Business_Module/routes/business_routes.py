from typing import List
from fastapi import APIRouter, Depends, Request

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
from src.Business_Module.dtos.business_dtos.business_dto import Business_DTO
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
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


business_routes = APIRouter(prefix="/business")


@business_routes.post(
    "/",
    response_model=Business_DTO,
    status_code=201,
)
async def create_business(
    business_payload: Create_Business_DTO,
    request: Request,
    create_business_use_case: Create_Business_Usecase = Depends(
        get_create_business_usecase
    ),
):
    controller = Create_Business_Controller(
        use_case=create_business_use_case, business_payload=business_payload
    )
    controller.access_control(request=request)
    return await controller.handle()


@business_routes.get(
    "/",
    response_model=List[Business_DTO],
    status_code=200,
)
async def list_all_business(
    request: Request,
    list_businesses_use_case: List_Businesses_Usecase = Depends(
        get_list_businesses_usecase
    ),
):
    controller = List_Businesses_Controller(use_case=list_businesses_use_case)
    return await controller.handle()


@business_routes.get(
    "/{id}",
    response_model=Business_DTO,
    status_code=200,
)
async def get_business_by_id(
    id: str,
    find_business_byId_use_case: Find_Business_By_Id_Usecase = Depends(
        find_business_by_id_usecase
    ),
):
    controller = Find_Business_ById_Controller(
        use_case=find_business_byId_use_case, id=id
    )
    return await controller.handle()


@business_routes.patch(
    "/{id}",
    response_model=Business_DTO,
    status_code=201,
)
async def update_business(
    id: str,
    business_payload: Update_Business_DTO,
    request: Request,
    update_business_use_case: Update_Business_Usecase = Depends(
        update_business_usecase
    ),
):
    controller = Update_Business_Controller(
        use_case=update_business_use_case, id=id, business_payload=business_payload
    )
    controller.access_control(request=request)
    return await controller.handle()


@business_routes.delete("/{id}", status_code=204)
async def delete_business(
    id: str,
    request: Request,
    delete_business_usecase: Delete_Business_Usecase = Depends(delete_business_usecase),
):
    controller = Delete_Business_Controller(
        use_case=delete_business_usecase, business_id=id
    )
    controller.access_control(request=request)
    return await controller.handle()
