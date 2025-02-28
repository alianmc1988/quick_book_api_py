import asyncio
from fastapi import FastAPI
import uvicorn
from configurations.config import settings

from database.db import init_db
from setup.api_router import bootstrap_routes
from setup.middlewares.middlewares import bootstrap_middlewares

async def init():
    try:
        await init_db()
        print("Database initialized")
    except Exception as e:
        print(f"Error initializing database: {e}")
        exit(1)

app = FastAPI()
bootstrap_routes(app)
bootstrap_middlewares(app)



if __name__ == "__main__":
    asyncio.run(init())
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)