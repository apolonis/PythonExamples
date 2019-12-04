from sqlalchemy import Column,Integer, String,create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
def dbCreate():
    engine = create_engine('postgresql+psycopg2://dcloud:dcl0ud2019@localhost:5432/dcloud_db')
    return engine

class User(Base):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=False)
    lastname = Column('lastname', String, unique=False)
    email = Column('email', String, unique=True)
    address = Column('address', String, unique=False)
    roles = Column('roles', String, unique=False)

    def __init__(self, name, lastname, email, address,roles):
        self.name = name
        self.lastname = lastname
        self. email = email
        self.address = address
        self.roles = roles

engine = dbCreate()
Base.metadata.create_all(bind=engine)