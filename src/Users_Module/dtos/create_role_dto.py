from enum import Enum
from uuid import UUID
from pydantic import BaseModel


class RoleDTO(Enum):
    OWNER = "OWNER"
    MANAGER = "MANAGER"
    SUPERVISOR = "SUPERVISOR"
    STAFF = "STAFF"


class Create_Role_DTO(BaseModel):
    user_id: UUID
    role_name: RoleDTO
    business_id: str | None = None

    def set_business_id(self, business_id: str) -> None:
        self.business_id = business_id

    class Config:
        orm_mode = True
