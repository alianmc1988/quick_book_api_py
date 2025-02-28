from sqlalchemy import Column, Enum, ForeignKey
from src.Users_Module.value_objects.Role_Type import (
    Staff_Role_Type_Enum,
    Staff_Role_literal_Enum,
    convert_numeric_to_literal_role,
)
from src.baseHandlers.Model_Entity import Base_Model


class Role(Base_Model):
    __tablename__ = "roles"
    role_number = Column(Enum(Staff_Role_Type_Enum), default=Staff_Role_Type_Enum.STAFF)
    user_id = Column(ForeignKey("users.id"))
    business_id = Column(ForeignKey("businesses.id"))

    def convert_numeric_to_literal_role(self) -> Staff_Role_literal_Enum:
        return convert_numeric_to_literal_role(role_number=self.role_number)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, role={self.convert_numeric_to_literal_role(self.role_number)}, user={self.user_id}, business={self.business_id})>"

    def __str__(self):
        return f"<User(id={self.id}, role={self.convert_numeric_to_literal_role(self.role_number)}, user={self.user_id}, business={self.business_id})>"
