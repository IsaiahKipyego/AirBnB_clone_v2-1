#!/usr/bin/python3
""" Place Module for HBNB project
"""


from models import storage_type as st, storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, FLOAT, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity",
    Column('place_id', String(60), Base.metadata,
           ForeignKey('places.id'), primary_key=True,  nullable=False),
    Column('amenity_id', String(60), Base.metadata,
           ForeignKey('amenities.id'), primary_key=True,  nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(FLOAT, default=0)
    longitude = Column(FLOAT, default=0)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []
    amenities = relationship("Amenity", viewonly=False)

    if st != 'db':
        @property
        def amenities(self):
            """returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

