from sqlalchemy import Column, Enum, ForeignKey, Integer
from src.Users_Module.value_objects.Role_Type import Staff_Role_Type_Enum
from src.baseHandlers.Model_Entity import Base_Model



class Role(Base_Model):
    __tablename__ = 'roles'
    role_number = Column(Enum(Staff_Role_Type_Enum), default=Staff_Role_Type_Enum.STAFF)
    user_id = Column(ForeignKey("users.id"))
    business_id = Column(ForeignKey("businesses.id"))



    def convert_numeric_to_literal_role(self):
        literal_roles_map:dict = {
            [Staff_Role_Type_Enum.SUDO]:"SUDO",
            [Staff_Role_Type_Enum.OWNER]:"OWNER",
            [Staff_Role_Type_Enum.MANAGER]:"MANAGER",
            [Staff_Role_Type_Enum.SUPERVISOR]:"SUPERVISOR",
            [Staff_Role_Type_Enum.STAFF]:"STAFF",

        }
        return literal_roles_map[self.role_number]

    def __repr__(self)->str:
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"<User(name={self.name}, email={self.email})>" 

    