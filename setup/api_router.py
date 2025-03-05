from typing import List
from fastapi import FastAPI, APIRouter
from src.Auth_Module.routes.auth_router import auth_routes
from src.Business_Module.routes.business_management_router import (
    business_management_routes,
)
from src.Users_Module.routes.user_router import user_routes

routers: List[APIRouter] = [user_routes, business_management_routes, auth_routes]


def bootstrap_routes(app: FastAPI) -> FastAPI:
    for router in routers:
        app.include_router(router)

    return app
