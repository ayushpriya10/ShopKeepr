from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import create_engine


class Database():
    engine = create_engine(f'sqlite:///packages.db', echo=True)
    meta = MetaData()
    packages = Table(
        'packages', meta,
        Column('pid', Integer, primary_key=True, autoincrement=True),
        Column('name', String),
        Column('version', String, nullable=True),
        Column('parent_id', String, nullable=True)
    )

    def initiate_engine(self):
        self.meta.create_all(self.engine)

        return self.packages, self.engine


if __name__ == '__main__':
    initiate_engine()
