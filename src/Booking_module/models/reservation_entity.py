from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.Booking_module.models.reservation_state_machine import (
    ReservationStateMachine,
    ReservationStatus,
)
from src.baseHandlers.Model_Entity import (
    Base_Model,
)


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
    start_at = Column(DateTime, nullable=False)
    ends_at = Column(DateTime, nullable=False)
    guests = Column(Integer, nullable=False)
    status = Column(
        Enum(ReservationStatus), default=ReservationStatus.CREATED, nullable=False
    )
    notes = Column(Text)

    business = relationship("Business", backref="reservations")
    space = relationship("Space", backref="reservations")
    user = relationship("User", backref="reservations")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_machine = ReservationStateMachine()
        self.status = self.state_machine.current_state.value

    def change_state(self, new_state: ReservationStatus):
        target_state = next(
            (state for state in self.state_machine.states if state.value == new_state),
            None,
        )
        if target_state is None:
            raise ValueError(f"Invalid state: {new_state}")
        transition_method = getattr(
            self.state_machine, f"to_{target_state.name.lower()}"
        )
        if transition_method:
            transition_method()
        else:
            raise ValueError(
                f"Invalid state transition: {self.state_machine.current_state.value} to {new_state}"
            )
        self.status = self.state_machine.current_state.value
