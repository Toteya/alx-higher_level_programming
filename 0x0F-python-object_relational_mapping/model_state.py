"""
Module model_state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column('id', Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column('name', String(128), nullable=False)

    # engine = create_engine('sqlite://')
    # Base
