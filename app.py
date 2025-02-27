import asyncio
from typing import Awaitable, Callable, List
from fastapi import FastAPI


class Api:
    def __init__(self,
                 app:FastAPI,
                 db_func:Callable[[],Awaitable[None]],
                middlewares: List[Callable[[FastAPI],FastAPI | None]] = [],  
                 routers: List[Callable[[FastAPI], FastAPI | None]] = [] ):
        self.app = app
        self.middlewares = middlewares
        self.db_func = db_func
        self.routers = routers


    async def connect_db(self):
        print ("Connecting to Database")
        try:
            await self.db_func()
            print("Database Connected successfully")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            exit(1)
            


    def bootstrap_middlewares(self)->FastAPI:
        print ("Initializing middlewares")
        for middleware in self.middlewares:
            middleware(self.app)
        print ("Middlewares initialized successfully")
        return self.app

    def bootstrap_router(self)->FastAPI:
        print ("Loading routes")
        for router in self.routers:
            self.app.include_router(router=router)
        print ("Routes loaded successfully")
        return self.app        


    def init(self)->FastAPI:
        print ("Api is setting up")
        asyncio.run(self.connect_db())
        self.bootstrap_middlewares()
        self.bootstrap_router()
        print ("Api is now prepared to run")
        return self.app