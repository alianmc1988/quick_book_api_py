from pydantic import BaseModel, EmailStr


class Login_DTO(BaseModel):
    email: EmailStr
    password: str
