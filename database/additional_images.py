from sqlalchemy import Integer, String, Column, ForeignKey, orm
from database.db_session import SqlAlchemyBase


class AdditionalImages(SqlAlchemyBase):
    __tablename__ = "additional_images"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    IMAGE = Column(String, nullable=True)
    AD_METRO_ID = Column(Integer, ForeignKey("ad_metro.ID"))
    AD_METRO = orm.relation("AdMetro")
