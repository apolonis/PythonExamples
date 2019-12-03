from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

def dbCreate():
    engine = create_engine('sqlite:///testAio1.db')
    return engine

Base = declarative_base()
class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    roles = Column(String)

    def __init__(self, username, password, roles):
        self.username = username
        self.password = password
        self.roles = roles

engine = dbCreate()
Base.metadata.create_all(engine)


