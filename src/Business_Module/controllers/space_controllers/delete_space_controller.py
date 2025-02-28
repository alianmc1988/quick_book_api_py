from src.Business_Module.services.space_usecases.delete_space_use_case import (
    Delete_Space_Usecase,
)

from src.baseHandlers.Controller import Base_Controller


class Delete_Space_Controller(Base_Controller):
    def __init__(self, use_case: Delete_Space_Usecase):
        self.use_case = use_case

    async def handle(self, id: str):
        result = await self.use_case.execute(id=id)
        return result
