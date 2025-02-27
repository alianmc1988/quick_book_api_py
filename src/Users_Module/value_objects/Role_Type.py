from enum import Enum


class Staff_Role_Type_Enum(Enum):
    SUDO = 0
    OWNER = 10
    MANAGER = 30
    SUPERVISOR = 50
    STAFF = 70