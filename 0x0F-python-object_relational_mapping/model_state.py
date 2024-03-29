#!/usr/bin/python3
"""
Module model_state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    id = Column('id', Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column('name', String(128), nullable=False)
