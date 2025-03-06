from fastapi import APIRouter, Depends
from setup.guards.auth_guard import authentication_middleware
from src.Business_Module.routes.space_routes import space_routes
from src.Business_Module.routes.business_routes import business_routes

business_management_routes = APIRouter(
    prefix="/business-management", tags=["Business Management API"]
)
business_management_routes.include_router(
    router=business_routes, dependencies=[Depends(authentication_middleware)]
)
business_management_routes.include_router(
    router=space_routes, dependencies=[Depends(authentication_middleware)]
)
