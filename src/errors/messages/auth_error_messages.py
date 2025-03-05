from sqlalchemy import Enum


class AuthErrorMessagesEnum(Enum):
    UNAUTHORIZED = "Invalid email or password"
    FORBIDEN = "User has no clearence to perform this operation"
