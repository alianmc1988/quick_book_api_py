from pydantic import BaseModel, EmailStr



class Update_User_DTO(BaseModel):
    name: str|None  = None
    email: EmailStr | None = None
    password: str | None = None
