from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///tst.db')

session = sessionmaker(bind=engine)()

Base = declarative_base()

class Person(Base):

    __tablename__ = "person"

    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# user = Person("Sasa","password")
# user1 = Person("Sanja","password01")
# user2 = Person("Ime","password02")
# session.add(user2)
# session.add(user1)
# session.add(user)
# session.commit()


result = session.query(User).all()
result1 = [r for r in session.query(User).all()]

for r in result1:
    print(r)
    print(r.username)

Base.metadata.create_all(engine)