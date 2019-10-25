from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

engine = create_engine('sqlite:///packages.db', echo=True)
meta = MetaData()

packages = Table(
    'packages', meta,
    Column('pid', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('version', String, nullable=True),
    Column('parent_id', String, nullable=True)
)

meta.create_all(engine)