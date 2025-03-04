from pydantic import BaseModel

from src.Users_Module.value_objects.Role_Type import Staff_Role_literal_Enum


class Role_DTO(BaseModel):
    type: Staff_Role_literal_Enum | None = None
