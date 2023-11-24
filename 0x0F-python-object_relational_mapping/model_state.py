#!/usr/bin/python3
"""
    Script that defines a state class and
    Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declareative_base

Base = declarative_base()

class State(Base):
    """
        State class

        Attributes:
            __tablename__ (str): The name of table
            id (int): The state id
            name (str): The state name
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
