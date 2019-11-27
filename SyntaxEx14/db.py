from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test6.db')


session = sessionmaker(bind=engine)()

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

'''user = User("Sasa","password")
user1 = User("Sanja","password01")
user2 = User("Ime","password02")
session.add(user2)
session.commit()'''


result = session.query(User).all()
result1 = [r for r in session.query(User).all()]

for r in result1:
    print(r)
    print(r.username)
#print(result)
#from pdb import set_trace; set_trace()

Base.metadata.create_all(engine)
