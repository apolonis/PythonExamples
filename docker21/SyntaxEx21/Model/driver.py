from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

#one to many
from sqlalchemy.orm import relationship

Base = declarative_base()
def dbCreate():
    engine = create_engine('postgresql+psycopg2://dcloud:dcl0ud2019@localhost:5432/dcloud_db')
    return engine

class Driver(Base):
    __tablename__ ='Driver'

    id = Column('id', Integer, primary_key=True)
    fullname = Column('fullname', String, unique=False, nullable=False)

    def __init__(self,fullname):
        self.fullname = fullname

engine = dbCreate()
Base.metadata.create_all(bind=engine)
