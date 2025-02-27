from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from setup.global_exception_middleware import global_exception_handler

def setUpCors(app: FastAPI) -> FastAPI:
    origins = [
        "http://localhost"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_methods=["*"],
        allow_credentials=True,
        allow_headers=["*"],
        allow_origins=origins
    )
    return app

middlewares = [
    setUpCors,
    global_exception_handler
]

def bootstrap_middlewares(app: FastAPI) -> FastAPI:
    for mid in middlewares:
        mid(app)
    return app