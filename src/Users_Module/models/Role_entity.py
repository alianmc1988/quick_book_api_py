from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from src.Users_Module.value_objects.Role_Type import (
    Staff_Role_Type_Enum,
    convert_numeric_to_literal_role,
)
from src.baseHandlers.Model_Entity import Base_Model


class Role(Base_Model):
    __tablename__ = "roles"
    role = Column(Integer, default=Staff_Role_Type_Enum.STAFF.value)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    business_id = Column(ForeignKey("businesses.id", ondelete="CASCADE"))

    @property
    def role_name(self) -> str:
        data = convert_numeric_to_literal_role(self.role).value

        return data

    def __repr__(self) -> str:
        return f"<Role(id={self.id}, role={self.role}, user={self.user_id}, business={self.business_id})>"

    def __str__(self):
        return f"<Role(id={self.id}, role={self.role}, user={self.user_id}, business={self.business_id})>"

    __table_args__ = (UniqueConstraint("business_id", "user_id", "role"),)
