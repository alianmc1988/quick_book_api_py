from enum import Enum


class Staff_Role_Type_Enum(Enum):
    SUDO = 0
    OWNER = 10
    MANAGER = 30
    SUPERVISOR = 50
    STAFF = 70


class Staff_Role_literal_Enum(Enum):
    SUDO = "SUDO"
    OWNER = "OWNER"
    MANAGER = "MANAGER"
    SUPERVISOR = "SUPERVISOR"
    STAFF = "STAFF"


def convert_numeric_to_literal_role(
    role_number: int,
) -> Staff_Role_literal_Enum:
    literal_roles_map: dict = {
        Staff_Role_Type_Enum.SUDO.value: Staff_Role_literal_Enum.SUDO,
        Staff_Role_Type_Enum.OWNER.value: Staff_Role_literal_Enum.OWNER,
        Staff_Role_Type_Enum.MANAGER.value: Staff_Role_literal_Enum.MANAGER,
        Staff_Role_Type_Enum.SUPERVISOR.value: Staff_Role_literal_Enum.SUPERVISOR,
        Staff_Role_Type_Enum.STAFF.value: Staff_Role_literal_Enum.STAFF,
    }
    role = literal_roles_map[role_number]
    return role


def conver_literal_to_numeric_role(
    role_name: Staff_Role_literal_Enum,
) -> Staff_Role_Type_Enum:
    role = Staff_Role_Type_Enum[role_name.value].value
    return role
