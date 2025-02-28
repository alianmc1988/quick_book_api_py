from fastapi import APIRouter
from src.Business_Module.routes.business_routes import business_routes

business_management_routes = APIRouter(prefix="/business-management", tags=["Business Management API"])
business_management_routes.include_router(router=business_routes)