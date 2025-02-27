from pydantic import BaseModel, EmailStr


class Create_User_DTO(BaseModel):
    name: str
    email: EmailStr
    password: str