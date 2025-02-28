from enum import Enum


class Business_Type_Enum(str, Enum):
    BAR = "bar"
    HOTEL = "hotel"
    RESTAURANT = "restaurant"


class Business_Social_Media_Enum(str, Enum):
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "tweeter"
    TIKTOK = "tiktok"
