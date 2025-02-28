from pydantic import BaseModel


class Role_DTO(BaseModel):
    type:str|None = None