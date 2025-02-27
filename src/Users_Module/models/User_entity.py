from sqlalchemy import Column, DateTime, func, LargeBinary
from sqlalchemy.types import String
from bcrypt import hashpw, gensalt, checkpw
from configurations.config import settings
from src.baseHandlers.Model_Entity import Base_Model


class User(Base_Model):
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
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
    


