from typing import Text
from pydantic import BaseModel

from src.Business_Module.value_objects.Space_Type import Space_Type_Enum


class Create_Space_DTO(BaseModel):
    name: str
    type: Space_Type_Enum
    capacity: int
    description: Text | None = None
    business_id: str | None = None

    def set_business_id(self, business_id: str) -> None:
        self.business_id = business_id

    class Config:
        orm_mode = True
