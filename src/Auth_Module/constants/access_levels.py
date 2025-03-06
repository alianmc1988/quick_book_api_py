from sqlalchemy import Enum


class AccessLevel(Enum):
    SUDO = 0
    OWNER = 10
    MANAGER = 30
    SUPERVISOR = 50
    STAFF = 70
    CLIENT = 100
    GUEST = 200
