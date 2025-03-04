from enum import Enum


class Staff_Role_Type_Enum(Enum):
    SUDO = 0
    OWNER = 10
    MANAGER = 30
    SUPERVISOR = 50
    STAFF = 70


class Staff_Role_literal_Enum(str, Enum):
    SUDO = "SUDO"
    OWNER = "OWNER"
    MANAGER = "MANAGER"
    SUPERVISOR = "SUPERVISOR"
    STAFF = "STAFF"


def convert_numeric_to_literal_role(
    role_number: Staff_Role_Type_Enum,
) -> Staff_Role_literal_Enum:
    literal_roles_map: dict = {
        Staff_Role_Type_Enum.SUDO: Staff_Role_literal_Enum.SUDO,
        Staff_Role_Type_Enum.OWNER: Staff_Role_literal_Enum.OWNER,
        Staff_Role_Type_Enum.MANAGER: Staff_Role_literal_Enum.MANAGER,
        Staff_Role_Type_Enum.SUPERVISOR: Staff_Role_literal_Enum.SUPERVISOR,
        Staff_Role_Type_Enum.STAFF: Staff_Role_literal_Enum.STAFF,
    }
    return literal_roles_map[role_number]


def conver_literal_to_numeric_role(
    role_name: Staff_Role_literal_Enum,
) -> Staff_Role_Type_Enum:
    numeric_roles_map: dict = {
        Staff_Role_literal_Enum.SUDO: Staff_Role_Type_Enum.SUDO,
        Staff_Role_literal_Enum.OWNER: Staff_Role_Type_Enum.OWNER,
        Staff_Role_literal_Enum.MANAGER:Staff_Role_Type_Enum.MANAGER,
        Staff_Role_literal_Enum.SUPERVISOR: Staff_Role_Type_Enum.SUPERVISOR,
        Staff_Role_literal_Enum.STAFF:Staff_Role_Type_Enum.STAFF,
    }
    role = numeric_roles_map[role_name]
    return role.value



