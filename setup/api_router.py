from fastapi import FastAPI, APIRouter
from users_api.routes.user_router import user_routes

routers = [user_routes]

def bootstrap_routes(app: FastAPI) -> FastAPI:
    for router in routers:
        app.include_router(router)
    
    return app
