from uuid import UUID
from pydantic import BaseModel

from src.Users_Module.value_objects.Role_Type import Staff_Role_literal_Enum


class Create_Role_DTO(BaseModel):
    user_id: UUID
    business_id: UUID
    role_name: Staff_Role_literal_Enum

    class Config:
        orm_mode = True
