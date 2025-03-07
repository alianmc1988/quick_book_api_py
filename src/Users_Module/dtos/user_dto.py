from typing import List
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

from src.Users_Module.dtos.role_dto import Role_DTO


class UserDTO(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    roles: List[Role_DTO] | None = None

    class Config:
        orm_mode = True
        from_attributes = True
