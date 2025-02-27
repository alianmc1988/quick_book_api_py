from pydantic import BaseModel, EmailStr

from users_api.dtos.create_user_dto import Create_User_DTO


class Update_User_DTO(BaseModel):
    name: str|None  = None
    email: EmailStr | None = None
    password: str | None = None
