from pydantic import BaseModel

from src.Business_Module.value_objects.Business_Type import (
    Business_Social_Media_Enum,
)


class Business_Media_DTO(BaseModel):
    type: Business_Social_Media_Enum
    profile: str
    business_id: str
