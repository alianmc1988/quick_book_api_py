import datetime
from typing import Text
from uuid import UUID
from pydantic import BaseModel

from src.Booking_module.value_objects.Reservation_Status import (
    ReservationStatusEnum,
)


class ReservationDTO(BaseModel):
    id: UUID
    user_id: UUID
    business_id: UUID
    start_at: datetime
    status: ReservationStatusEnum
    guests: int
    notes: Text
