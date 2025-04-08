from enum import Enum


class ReservationStatusEnum(Enum):
    CREATED = "created"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
