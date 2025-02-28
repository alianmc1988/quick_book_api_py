from src.Business_Module.services.busines_usecases.list_businesses_use_case import List_Businesses_Usecase
from src.baseHandlers.Controller import Base_Controller


class List_Businesses_Controller(Base_Controller):
    def __init__(self, use_case: List_Businesses_Usecase):
        self.use_case=use_case

    async def handle(self):
        return await self.use_case.execute()