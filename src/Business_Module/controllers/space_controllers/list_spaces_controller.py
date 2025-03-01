from src.Business_Module.services.space_usecases.list_spaces_use_case import (
    List_Spaces_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class List_Spaces_Controller(Base_Controller):
    def __init__(self, use_case: List_Spaces_Usecase):
        self.use_case = use_case

    async def handle(self, business_id: str):
        return await self.use_case.execute(business_id=business_id)
