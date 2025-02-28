from src.Business_Module.services.space_usecases.find_space_byId_use_case import (
    Find_Space_ById_Usecase,
)
from src.baseHandlers.Controller import Base_Controller


class Find_Space_ById_Controller(Base_Controller):
    def __init__(self, use_case: Find_Space_ById_Usecase):
        self.use_case = use_case

    async def handle(self, id: str):
        result = await self.use_case.execute(space_id=id)
        return result
