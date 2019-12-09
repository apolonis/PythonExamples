from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from Model import driver
Base = declarative_base()
#   many to one
class Car(Base):
    __tablename__ ='car'

    id = Column('id', Integer, primary_key=True)
    model = Column('model', String, unique=False, nullable=False)
    # this is a foreign key for connection to other table
    driver_id = Column(Integer, ForeignKey(driver.Driver.id), nullable=False)

    def __init__(self, model,driver_id):
        self.model = model
        self.driver_id = driver_id

engine = driver.dbCreate()
Base.metadata.create_all(bind=engine)
