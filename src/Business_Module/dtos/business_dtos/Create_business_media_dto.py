from pydantic import BaseModel, EmailStr

from src.Business_Module.value_objects.Business_Type import Business_Social_Media_Enum, Business_Type_Enum


class Business_Media_DTO(BaseModel):
    type: Business_Social_Media_Enum
    profile:str
    business_id:str



