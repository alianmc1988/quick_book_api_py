from typing import List
from uuid import UUID
from pydantic import BaseModel, EmailStr

from src.Business_Module.dtos.business_dtos.social_Media_DTO import (
    Business_Social_Media_DTO,
)
from src.Business_Module.value_objects.Business_Type import Business_Type_Enum


class Business_DTO(BaseModel):
    id: UUID
    name: str
    address: str
    type: Business_Type_Enum
    phone: str
    other_phone: str | None = None
    email: EmailStr
    social_medias: List[Business_Social_Media_DTO] | None = None
