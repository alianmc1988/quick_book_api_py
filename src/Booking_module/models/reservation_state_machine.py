# create a state machine to handle reservation status
from enum import Enum
from statemachine import State, StateMachine


class ReservationStatus(Enum):
    CREATED = "created"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class ReservationStateMachine(StateMachine):
    created = State(ReservationStatus.CREATED, initial=True)
    pending = State(ReservationStatus.PENDING)
    confirmed = State(ReservationStatus.CONFIRMED)
    cancelled = State(ReservationStatus.CANCELLED)
    completed = State(ReservationStatus.COMPLETED)

    created.to(pending)
    pending.to(confirmed) | pending.to(cancelled)
    confirmed.to(completed) | confirmed.to(cancelled)
    cancelled.to(created)
