
from fastapi import APIRouter, Depends

from src.Business_Module.controllers.business_controllers.create_business_controller import Create_Business_Controller
from src.Business_Module.dtos.business_dtos.business_dto import Business_DTO
from src.Business_Module.dtos.business_dtos.create_business_dto import Create_Business_DTO
from src.Business_Module.services.busines_usecases.create_business_use_case import Create_Business_Usecase, get_create_business_usecase


business_routes = APIRouter(prefix="/business" )

@business_routes.post("/", response_model=Business_DTO, status_code=201)
async def create_business(business_payload: Create_Business_DTO, create_business_use_case: Create_Business_Usecase = Depends(get_create_business_usecase)):
    controller = Create_Business_Controller(use_case=create_business_use_case)
    return await controller.handle(business_payload=business_payload)