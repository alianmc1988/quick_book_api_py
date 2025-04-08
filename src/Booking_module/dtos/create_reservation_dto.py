from typing import Text

from pydantic import BaseModel


class CreateReservationDto(BaseModel):
    start_at: str
    business_id: int
    guests: int
    notes: Text
