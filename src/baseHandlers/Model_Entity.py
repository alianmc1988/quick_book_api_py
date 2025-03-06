import uuid
from sqlalchemy import UUID, Column, DateTime, func
from database.db import Base


class Base_Model(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    def soft_delete(self, logged_user: str) -> None:
        self.deleted_at = func.now()
        self.updated_by = logged_user

    def restore(self) -> None:
        self.deleted_at = None
