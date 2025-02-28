from sqlalchemy import  CheckConstraint, Column, ForeignKey,  Integer, String, Text,  Boolean, Enum
from src.baseHandlers.Model_Entity import Base_Model
from src.Business_Module.value_objects.Business_Type import Business_Type_Enum


class Space(Base_Model):
    __tablename__ = 'spaces'
    name = Column(String, nullable=False)
    type = Column(Enum(Business_Type_Enum))
    isActive = (Column(Boolean, default=True))
    capacity = Column(Integer, nullable=False )
    description = Column(Text, nullable=True)
    business_id = Column(ForeignKey("businesses.id"))

    def __repr__(self)->str:
        return f"<Space(id={self.id}, name='{self.name}')>"

    __table_args__=(
        CheckConstraint("capacity > 1 AND capacity < 20000", name="check_capacity_range"),
        CheckConstraint("char_length(description) <= 250", name="check_description_length")
    )