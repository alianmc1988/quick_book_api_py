from pydantic import BaseModel
from src.Users_Module.dtos.user_dto import UserDTO


class Auth_DTO(BaseModel):
    access_token: str
    token_type: str
    user: UserDTO

    class Config:
        orm_mode = True
        from_attributes = True
