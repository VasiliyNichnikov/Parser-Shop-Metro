from sqlalchemy import Column, Integer, String, Float, orm
from database.db_session import SqlAlchemyBase


class AdMetro(SqlAlchemyBase):
    __tablename__ = "ad_metro"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ARTICLE_NUMBER = Column(Integer, nullable=True)
    NAME = Column(String, nullable=True)
    PRICE = Column(Float, nullable=True)
    PRICE_WITHOUT_DISCOUNT = Column(Float, nullable=True)
    WEIGHT = Column(String, nullable=True)
    PACKING_WIDTH = Column(Float, nullable=True)
    PACKING_HEIGHT = Column(Float, nullable=True)
    PACKING_LENGTH = Column(Float, nullable=True)
    MAIN_IMAGE = Column(String, nullable=True)
    ADDITIONAL_IMAGES = Column(String, nullable=True)
    ARTICLE_IMAGES = Column(String, nullable=True)
    # ADDITIONAL_IMAGES = orm.relation("AdditionalImages", back_populates="AD_METRO")
    # ARTICLE_IMAGES = orm.relation("ArticleImages", back_populates="AD_METRO")
    TYPE_PRODUCT = Column(String, nullable=True)
    TYPE_OF_PACKAGING = Column(String, nullable=True)
    MINIMUM_STORAGE_TEMPERATURE = Column(String, nullable=True)
    MAXIMUM_STORAGE_TEMPERATURE = Column(String, nullable=True)
    SHELF_LIFE = Column(Integer, nullable=True)
    BRAND = Column(String, nullable=True)
    STRUCTURE = Column(String, nullable=True)
    ANNOTATION = Column(String, nullable=True)
    COUNTRY = Column(String, nullable=True)
    ENERGY_VALUE = Column(String, nullable=True)
