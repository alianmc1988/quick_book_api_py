from fastapi import Depends
from src.Auth_Module.constants.access_levels import AccessLevel
from src.Users_Module.dtos.create_role_dto import Create_Role_DTO
from src.Users_Module.models.User_entity import User
from src.Users_Module.services.add_role_to_user_usecase import Create_Role_Usecase
from src.baseHandlers.Controller import Base_Controller

from src.Users_Module.services.create_user_usecase import (
    Create_User_Usecase,
    get_create_user_use_case,
)


class Create_Role_Controller(Base_Controller):
    def __init__(
        self, create_role_use_case: Create_Role_Usecase, role_payload: Create_Role_DTO
    ):
        super().__init__(access_level=AccessLevel.MANAGER)
        self.create_role_use_case = create_role_use_case
        self.role_payload = role_payload

    async def define(self) -> User:
        self.role_payload.set_business_id(business_id=self.ctx)
        return await self.create_role_use_case.execute(
            user_id=self.role_payload.user_id,
            business_id=self.role_payload.business_id,
            role=self.role_payload.role_name,
        )


def get_create_user_controller(
    create_user_use_case: Create_User_Usecase = Depends(get_create_user_use_case),
):
    return Create_Role_Controller(create_user_use_case=create_user_use_case)
