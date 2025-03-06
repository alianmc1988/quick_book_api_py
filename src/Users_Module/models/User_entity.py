from sqlalchemy import Column, LargeBinary
from .Role_entity import Role
from sqlalchemy.types import String, BOOLEAN
from bcrypt import hashpw, gensalt, checkpw
from configurations.config import settings
from src.baseHandlers.Model_Entity import Base_Model
from sqlalchemy.orm import relationship
from passlib.context import CryptContext


class User(Base_Model):
    __tablename__ = "users"
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    roles = relationship("Role", backref="users", lazy="selectin")
    is_master = Column(BOOLEAN, default=False)

    def __repr__(self) -> str:
        return f"<User(name={self.name}, email={self.email})>"

    def __str__(self):
        return f"<User(name={self.name}, email={self.email})>"

    def is_master_user(self):
        return self.is_master

    def hash_password(self):
        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.password = bcrypt_context.hash(self.password)

    def verify_password(self, password: str) -> bool:
        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        result = bcrypt_context.verify(password, self.password)
        return result
