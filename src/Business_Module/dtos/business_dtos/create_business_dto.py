from pydantic import BaseModel, EmailStr

from src.Business_Module.value_objects.Business_Type import Business_Type_Enum


class Create_Business_DTO(BaseModel):
    name: str
    address: str
    type: Business_Type_Enum
    phone: str
    other_phone: str | None = None
    email: EmailStr
