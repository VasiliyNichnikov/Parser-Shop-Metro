from sqlalchemy import Integer, String, orm, ForeignKey, Column
from database.db_session import SqlAlchemyBase


class ArticleImages(SqlAlchemyBase):
    __tablename__ = "article_images"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ARTICLE = Column(String, primary_key=False)
    AD_METRO_ID = Column(Integer, ForeignKey("ad_metro.ID"))
    AD_METRO = orm.relation("AdMetro")
