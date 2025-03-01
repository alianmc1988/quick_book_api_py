from typing import Text
from pydantic import BaseModel

from src.Business_Module.value_objects.Space_Type import Space_Type_Enum


class Update_Space_DTO(BaseModel):
    name: str | None = None
    type: Space_Type_Enum | None = None
    capacity: int | None = None
    description: Text | None = False
