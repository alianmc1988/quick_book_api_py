import uuid
from database.db import Base
from sqlalchemy import Column, DateTime, Text, func, LargeBinary, Null
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import String
from bcrypt import hashpw, gensalt, checkpw
from configurations.config import settings


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)


    def __repr__(self)->str:
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"<User(name={self.name}, email={self.email})>" 

    def hash_password(self):
        self.password = hashpw(self.password.encode('utf-8'), gensalt(rounds=settings.SALT_ROUNDS)) 
    
    async def verify_password(self, password: str) -> bool:
        return checkpw(password.encode('utf-8'), self.password.tobytes())
    
    def soft_delete(self):
        self.deleted_at = func.now()
    
    def restore(self):
        self.deleted_at = None
    


