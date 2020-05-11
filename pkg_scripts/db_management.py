# from sqlalchemy import MetaData
# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy import create_engine
#
#
# class Database():
#     engine = create_engine(f'sqlite:///packages.db', echo=True)
#     meta = MetaData()
#     packages = Table(
#         'packages', meta,
#         Column('pid', Integer, primary_key=True, autoincrement=True),
#         Column('name', String),
#         Column('version', String, nullable=True),
#         Column('parent_id', String, nullable=True)
#     )
#
#     def initiate_engine(self):
#         self.meta.create_all(self.engine)
#
#         return self.packages, self.engine
#
#
# if __name__ == '__main__':
#     initiate_engine()


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'sqlite:///packages.db', echo=True)
Base = declarative_base()
Session = sessionmaker(engine)

session = Session()


class Requirements(Base):
    __tablename__ = 'requirements'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=True)
    parent_id = Column(String, nullable=True)

    def __repr__(self):
        if self.parent_id is not None:
            parent_dependency = session.query(Requirements.id.is_(self.parent_id)).first()
            return f"Requirement<id={self.id}, name={self.name}, version={self.version}, parent dependency ={parent_dependency.name}> "


def initialize_db():
    Base.metadata.create_all(engine)
    print("Database Initialized")
