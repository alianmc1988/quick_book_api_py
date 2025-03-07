from http.client import HTTPException
from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    Boolean,
    Enum,
    UniqueConstraint,
)
from src.Business_Module.value_objects.Space_Type import Space_Type_Enum
from src.baseHandlers.Model_Entity import Base_Model


class Space(Base_Model):
    __tablename__ = "spaces"
    name = Column(String, nullable=False)
    type = Column(Enum(Space_Type_Enum))
    isActive = Column(Boolean, default=True)
    capacity = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    business_id = Column(ForeignKey("businesses.id", ondelete="CASCADE"))
    available = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"<Space(id={self.id}, name='{self.name}')>"

    __table_args__ = (
        UniqueConstraint("name", "business_id"),
        CheckConstraint(
            "capacity > 1 AND capacity < 20000", name="check_capacity_range"
        ),
        CheckConstraint(
            "char_length(description) <= 250", name="check_description_length"
        ),
    )

    def book_space(self) -> None:
        if not self.isActive:
            raise HTTPException(status_code=422, detail="Space is not active")
        if self.isActive:
            self.available = False
            return
        raise HTTPException(status_code=422, detail="Space is already booked")
