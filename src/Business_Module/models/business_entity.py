from sqlalchemy import  Column, DateTime, String, func, Boolean, Enum as SQLAlchemyEnum
from src.baseHandlers.Model_Entity import Base_Model
from src.Business_Module.value_objects.Business_Type import Business_Type_Enum
from sqlalchemy.orm import relationship



class Business(Base_Model):
    __tablename__ = 'businesses'
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    type = Column(SQLAlchemyEnum(Business_Type_Enum), nullable=False)
    isActive = Column(Boolean, default=True)
    deleted_at = Column(DateTime, nullable=True)
    spaces  = relationship("Space", backref="business", lazy='selectin')
    phone = Column(String,nullable=False, unique=True)
    other_phone = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    social_medias = relationship("Business_Social_Media", backref="business", lazy='selectin')
    roles = relationship("Role", backref="business", lazy='selectin')

    def __repr__(self):
        return f"<Business(id={self.id}, name='{self.name}')>"


    ___table_args__ = {'extend_existing': True} 

    def soft_delete(self):
        self.deleted_at = func.now()
    
    def restore(self):
        self.deleted_at = None