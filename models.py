from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Country = Column(String)
