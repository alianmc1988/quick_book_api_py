from bcrypt import gensalt, hashpw
from pydantic import BaseModel
from configurations.config import settings
from sqlalchemy.ext.declarative import DeclarativeMeta as SqlAlchemyModel




def update_object_entity(payload_obj:dict, entity_to_update:SqlAlchemyModel):
    for key, value in payload_obj.items():
        if key == 'password':
            value = hashpw(value.encode('utf-8'), gensalt(rounds=settings.SALT_ROUNDS))
        setattr(entity_to_update, key, value)
    return entity_to_update