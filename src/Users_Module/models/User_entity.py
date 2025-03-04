from sqlalchemy import Column, LargeBinary
from .Role_entity import Role
from sqlalchemy.types import String
from bcrypt import hashpw, gensalt, checkpw
from configurations.config import settings
from src.baseHandlers.Model_Entity import Base_Model
from sqlalchemy.orm import relationship


class User(Base_Model):
    __tablename__ = "users"
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    roles = relationship("Role", backref="users", lazy="selectin")

    def __repr__(self) -> str:
        return f"<User(name={self.name}, email={self.email})>"

    def __str__(self):
        return f"<User(name={self.name}, email={self.email})>"

    def hash_password(self):
        self.password = hashpw(
            self.password.encode("utf-8"), gensalt(rounds=settings["SALT_ROUNDS"])
        )

    async def verify_password(self, password: str) -> bool:
        return checkpw(password.encode("utf-8"), self.password.tobytes())
