from sqlalchemy import Column, ForeignKey, Enum as SQLAlchemyEnum, UniqueConstraint
from src.Business_Module.value_objects.Feature_Toggle_type import Feature_Toggle_Enum
from src.baseHandlers.Model_Entity import Base_Model


class Business_feature_toggle(Base_Model):
    __tablename__ = "business_feature_toggles"
    feature_name = Column(SQLAlchemyEnum(Feature_Toggle_Enum), nullable=False)
    business_id = Column(ForeignKey("businesses.id"))

    def __repr__(self) -> str:
        return f"<FeatureToggle_id(id={self.id}, feature_name='{self.feature_name}')>"

    __table_args__ = (UniqueConstraint("feature_name", "business_id"),)
