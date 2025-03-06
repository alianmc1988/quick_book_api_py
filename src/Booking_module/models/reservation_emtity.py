from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from database.db import (
    Base,
)
from src.baseHandlers.Model_Entity import (
    Base_Model,
)


class ReservationStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class Reservation(Base_Model):
    __tablename__ = "reservations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(
        UUID(as_uuid=True),
        ForeignKey("business.id", ondelete="CASCADE"),
        nullable=False,
    )
    space_id = Column(
        UUID(as_uuid=True), ForeignKey("spaces.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    guests = Column(Integer, nullable=False)
    status = Column(
        Enum(ReservationStatus), default=ReservationStatus.PENDING, nullable=False
    )
    notes = Column(Text)

    # Relaciones
    venue = relationship("Venue", back_populates="reservations")
    user = relationship("User", back_populates="reservations")
