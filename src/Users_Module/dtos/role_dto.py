from uuid import UUID
from pydantic import BaseModel


class Role_DTO(BaseModel):
    id: UUID
    user_id: UUID
    business_id: UUID
    role_name: str | None = None

    def __str__(self):
        return self.id

    class Config:
        orm_mode = True
        from_attributes = True
