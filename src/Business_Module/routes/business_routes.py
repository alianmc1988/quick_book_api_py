
from typing import List
from fastapi import APIRouter, Depends

from src.Business_Module.controllers.business_controllers.create_business_controller import Create_Business_Controller
from src.Business_Module.controllers.business_controllers.get_business_byId_controller import Get_Business_ById_Controller
from src.Business_Module.controllers.business_controllers.list_businesses_controller import List_Businesses_Controller
from src.Business_Module.dtos.business_dtos.business_dto import Business_DTO
from src.Business_Module.dtos.business_dtos.create_business_dto import Create_Business_DTO
from src.Business_Module.services.busines_usecases.create_business_use_case import Create_Business_Usecase, get_create_business_usecase
from src.Business_Module.services.busines_usecases.get_business_by_id_use_case import Get_Business_ById_Usecase, get_business_byId_usecase
from src.Business_Module.services.busines_usecases.list_businesses_use_case import List_Businesses_Usecase, get_list_businesses_usecase


business_routes = APIRouter(prefix="/business" )

@business_routes.post("/", response_model=Business_DTO, status_code=201)
async def create_business(business_payload: Create_Business_DTO, create_business_use_case: Create_Business_Usecase = Depends(get_create_business_usecase)):
    controller = Create_Business_Controller(use_case=create_business_use_case)
    return await controller.handle(business_payload=business_payload)

@business_routes.get("/", response_model=List[Business_DTO], status_code=200)
async def list_all_business(list_businesses_use_case: List_Businesses_Usecase = Depends(get_list_businesses_usecase)):
    controller = List_Businesses_Controller(use_case=list_businesses_use_case)
    return await controller.handle()

@business_routes.get("/{id}", response_model=Business_DTO, status_code=200)
async def get_business_by_id(get_business_byId_use_case: Get_Business_ById_Usecase = Depends(get_business_byId_usecase)):
    controller = Get_Business_ById_Controller(use_case=get_business_byId_use_case)
    return await controller.handle()