from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine


engine = create_engine("sqlite:///:memory:", echo=False)

metadata = MetaData()

product_table = Table("products", metadata,
                      Column("id", Integer, primary_key=True),
                      Column("name", String))

