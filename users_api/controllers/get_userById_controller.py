from typing import Annotated
from fastapi import Depends

from users_api.services.get_user_byId_usecase import Get_UserById_Usecase, get_userById_use_case
from users_api.services.softDelete_user_usecase import SoftDelete_User_Usecase, get_softDelete_user_use_case

class Get_UserById_Controller:
    def __init__(self, get_UserById_Usecase:Get_UserById_Usecase):
        self.get_UserById_Usecase = get_UserById_Usecase

    async def handle(self, id:str):
        return await self.get_UserById_Usecase.execute(id)
    

def get_userById_controller(get_UserById_Usecase:Get_UserById_Usecase = Depends(get_userById_use_case)):
    return Get_UserById_Controller(get_UserById_Usecase=get_UserById_Usecase)

TypeCreateUserController = Annotated[Get_UserById_Controller, Depends(get_userById_controller)]

   