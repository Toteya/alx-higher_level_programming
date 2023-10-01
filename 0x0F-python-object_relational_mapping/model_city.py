#!/usr/bin/python3
"""
module model_city
"""

from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "cities"
    id = Column('id', Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
    state = relationship("State", back_populates="cities")
