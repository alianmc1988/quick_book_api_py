from typing import Text
from uuid import UUID
from pydantic import BaseModel

from src.Business_Module.value_objects.Space_Type import Space_Type_Enum


class Space_DTO(BaseModel):
    id: UUID
    name: str
    type: Space_Type_Enum
    capacity: int
    description: Text | None = False
    business_id: UUID
