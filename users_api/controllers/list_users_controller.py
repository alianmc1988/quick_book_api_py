from fastapi import Depends, HTTPException

from users_api.services.list_users_usecase import get_list_users_use_case, List_Users_Usecase

class List_Users_Controller:
    def __init__(self, list_users_usecase:List_Users_Usecase):
        self.list_users_usecase = list_users_usecase

    async def handle(self):
        try:
            return await self.list_users_usecase.execute()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    

def get_list_users_controller(list_users_use_case:List_Users_Usecase = Depends(get_list_users_use_case)):
    return List_Users_Usecase(list_users_usecase=list_users_use_case)


   