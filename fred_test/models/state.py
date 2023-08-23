#!/usr/bin/python3
"""State Module for HBNB project
"""


from models import storage_type as st_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')

    if st_type == 'db':
        @property
        def cities(self):
            """returns the list of City instances with state_id equals
            to the current State.id"""
            from models import storage
            from models.city import City

            cities = storage.all(City)
            return [city for city in cities if city.state_id == self.id]
