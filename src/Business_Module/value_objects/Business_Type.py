from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


class Business_Type_Enum(str,Enum):
    BAR = "bar"
    HOTEL = "hotel"

class Business_Social_Media_Enum(str,Enum):
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "tweeter"
    TIKTOK = "tiktok"