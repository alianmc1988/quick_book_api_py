from pydantic import BaseModel


class FeatureToggleDto(BaseModel):
    name: str

    class Config:
        orm_mode = True
