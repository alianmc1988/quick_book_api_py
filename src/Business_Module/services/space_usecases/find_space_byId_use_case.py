from fastapi import Depends
from src.Business_Module.models.business_entity import Business
from src.Business_Module.repository.space_repository import Space_Repository, get_space_repository
from src.baseHandlers.Use_Case import Base_Use_Case


class Find_Space_ById_Usecase(Base_Use_Case):
    def __init__(self, space_repository: Space_Repository):
        self.space_repository = space_repository

    async def execute(self, space_id:str)-> Business:
        return await self.space_repository.find_space_by_id(space_id= space_id)
    
def get_find_space_byId_usecase(
       space_repository: Space_Repository = Depends(get_space_repository),
)->Find_Space_ById_Usecase:
    return Find_Space_ById_Usecase(space_repository=space_repository)