#!/usr/bin/python3
""" Place Module for HBNB project
    class attribute __tablename__
        represents the table name, places



        class attribute latitude
            represents a column containing a float
            can be null
        class attribute longitude
        represents a column containing a float
        can be null
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, FLOAT, ForeignKey
from sqlalchemy.orm import relationship


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
