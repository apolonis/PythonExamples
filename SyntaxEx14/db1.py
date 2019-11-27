from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "person"
    
    #def __init__(self, id, username):

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

# engine = create_engine('sqlite:///test1.db', echo=True)

# pip install psycopg2
# engine = create_engine('postgresql+psycopg2://postgres:admin@192.168.1.92:5432/test')
engine = create_engine('postgresql+psycopg2://postgres:admin@127.0.0.1:5432/test')

# ovo ce da kreira tabelu
Base.metadata.create_all(bind=engine)
# sa ovim ce da se izvrse sve promene sa povezanom tabelom
Session = sessionmaker(bind=engine)

session = Session()

user = User()
user.id = 10
user.username = "Sanja"

session.add(user)
session.commit()

session.close()

