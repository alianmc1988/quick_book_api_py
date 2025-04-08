from fastapi import Depends
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession


from src.Booking_module.dtos.create_reservation_dto import CreateReservationDto


class ReservationRepository:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def create_reservation(
        self, reservation: CreateReservationDto, created_by: str
    ):
        pass
