#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """a getter for instances of city with state_id equal
            to the current State.id"""
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(item)

            return cities
