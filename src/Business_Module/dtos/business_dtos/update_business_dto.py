from pydantic import BaseModel, EmailStr

from src.Business_Module.value_objects.Business_Type import Business_Type_Enum


class Update_Business_DTO(BaseModel):
    name:str | None = None
    address:str | None = None
    type:Business_Type_Enum | None = None
    phone:str | None = None
    other_phone:str | None = None
    email:EmailStr | None = None
