from server import server
from sqlalchemy.orm import sessionmaker
from model import user

engine = user.dbCreate()
session = sessionmaker(bind=engine)()

while True:
    my_dict = server.run_server()
    name = my_dict.get("name")
    lastname = my_dict.get("lastname")
    user_obj = user.User(name,lastname)

    session.add(user_obj)
    session.commit()




