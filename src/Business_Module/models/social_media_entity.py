from sqlalchemy import  CheckConstraint, Column, DateTime, ForeignKey, String, func, Boolean, Enum as SQLAlchemyEnum
from src.Business_Module.value_objects.Business_Type import Business_Type_Enum
from src.baseHandlers.Model_Entity import Base_Model
from src.Business_Module.value_objects.Business_Type import Business_Social_Media_Enum
from sqlalchemy.orm import relationship


class Business_Social_Media(Base_Model):
    __tablename__ = 'business_social_medias'
    type = Column(SQLAlchemyEnum(Business_Social_Media_Enum), nullable=False)
    profile = Column(String, nullable=False)
    business_id = Column(ForeignKey("businesses.id"))

    def __repr__(self):
        return f"<Business(id={self.id}, name='{self.type}')>"