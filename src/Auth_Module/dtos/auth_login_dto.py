from pydantic import BaseModel, EmailStr


class AuthLogin_DTO(BaseModel):
    email: EmailStr
    password: str
