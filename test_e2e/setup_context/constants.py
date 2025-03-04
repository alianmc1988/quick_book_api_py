from typing import List
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.dtos.role_dto import Role_DTO
from src.Users_Module.models.User_entity import User


class ContextPayload:
    clients: List[Create_User_DTO] | None = None
    staffs: List[User] | None = None
    roles: List[Role_DTO] | None = None
    spaces: List[Create_Space_DTO] | None = None
    businesses: List[Create_Business_DTO] | None = None
