from typing import List
from fastapi import FastAPI, APIRouter
from src.Users_Module.routes.user_router import user_routes

routers:List[APIRouter] = [user_routes]

def bootstrap_routes(app: FastAPI) -> FastAPI:
    for router in routers:
        app.include_router(router)
    
    return app
