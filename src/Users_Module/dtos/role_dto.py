from uuid import UUID
from pydantic import BaseModel

from src.Users_Module.value_objects.Role_Type import Staff_Role_literal_Enum


class Role_DTO(BaseModel):
    id: UUID
    user_id: UUID
    business_id: UUID
    role_name: str | None = None

    def __str__(self):
        return self.id

    # def role_Type(self):
    #     return Staff_Role_literal_Enum(self.role_number)

    class Config:
        orm_mode = True
