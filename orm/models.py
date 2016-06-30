from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """A user"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

