from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
def dbCreate():
    engine = create_engine('postgresql+psycopg2://dcloud:dcloud2019@localhost:5432/dcloud_v1')
    return engine

class User(Base):
    __tablename__ = 'Users'

    id = Column('id', Integer, primary_key = True)
    name = Column('name', String, unique=False, nullable=False)
    lastname = Column('lastname', String, unique=False, nullable=False)

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

engine = dbCreate()
Base.metadata.create_all(bind=engine)