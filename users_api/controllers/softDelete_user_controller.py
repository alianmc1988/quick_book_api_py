from typing import Annotated
from fastapi import Depends

from users_api.services.softDelete_user_usecase import SoftDelete_User_Usecase, get_softDelete_user_use_case

class SoftDelete_User_Controller:
    def __init__(self, softDelete_User_Usecase:SoftDelete_User_Usecase):
        self.softDelete_User_Usecase = softDelete_User_Usecase

    async def handle(self, id:str):
        return await self.softDelete_User_Usecase.execute(id)
    

def get_softDelete_user_controller(softDelete_User_Usecase:SoftDelete_User_Usecase = Depends(get_softDelete_user_use_case)):
    return SoftDelete_User_Controller(softDelete_User_Usecase=softDelete_User_Usecase)

TypeCreateUserController = Annotated[SoftDelete_User_Controller, Depends(get_softDelete_user_controller)]

   