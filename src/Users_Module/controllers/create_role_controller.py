from typing import Annotated
from fastapi import Depends
from src.Users_Module.models.User_entity import User
from src.Users_Module.services.add_role_to_user_usecase import Create_Role_Usecase
from src.Users_Module.value_objects.Role_Type import Staff_Role_literal_Enum
from src.baseHandlers.Controller import Base_Controller
from src.Users_Module.dtos.create_user_dto import Create_User_DTO

from src.Users_Module.services.create_user_usecase import (
    Create_User_Usecase,
    get_create_user_use_case,
)


class Create_Role_Controller(Base_Controller):
    def __init__(self, create_role_use_case: Create_Role_Usecase):
        self.create_role_use_case = create_role_use_case

    async def handle(self, user_id: str, business_id: str, role: Staff_Role_literal_Enum) -> User:
        return await self.create_role_use_case.execute(user_id=user_id, business_id=business_id, role=role)


def get_create_user_controller(
    create_user_use_case: Create_User_Usecase = Depends(get_create_user_use_case),
):
    return Create_Role_Controller(create_user_use_case=create_user_use_case)

