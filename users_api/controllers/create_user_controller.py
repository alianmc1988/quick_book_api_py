from typing import Annotated
from fastapi import Depends, HTTPException
from database.db import get_db
from users_api.dtos.create_user_dto import Create_User_DTO
from sqlalchemy.ext.asyncio import  AsyncSession

from users_api.repository.User_repository import UserRepository, get_user_repository
from users_api.services.create_user_usecase import Create_User_Usecase, get_create_user_use_case





# class Create_User_Controller:
#     def __init__(self, userRepo:UserRepository, db:AsyncSession):
#         self.userRepo = userRepo
#         self.db = db

#     async def handle(self, user: Create_User_DTO):
#         try:
#             return await self.userRepo.create_user(user, self.db)
#         except Exception as e:
#             raise HTTPException(status_code=400, detail=str(e))
    

# def get_create_user_controller(userRepo:UserRepository = Depends(get_user_repository), db:AsyncSession = Depends(get_db)):
#     return Create_User_Controller(userRepo=userRepo, db=db)

# TypeCreateUserController = Annotated[Create_User_Controller, Depends(get_create_user_controller)]

class Create_User_Controller:
    def __init__(self, create_user_use_case:Create_User_Usecase):
        self.create_user_use_case = create_user_use_case

    async def handle(self, user: Create_User_DTO):
        try:
            return await self.create_user_use_case.execute(user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    

def get_create_user_controller(create_user_use_case:Create_User_Usecase = Depends(get_create_user_use_case)):
    return Create_User_Controller(create_user_use_case=create_user_use_case)

TypeCreateUserController = Annotated[Create_User_Controller, Depends(get_create_user_controller)]

   