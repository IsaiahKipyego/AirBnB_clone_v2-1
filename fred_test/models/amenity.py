#!/usr/bin/python3
""" State Module for HBNB project
Add or replace in the class Amenity:
    class attribute __tablename__
        represents the table name, amenities
    class attribute name
        represents a column containing a string (128 characters)
        can't be null
    class attribute place_amenities must represent a relationship
    Many-To-Many between the class Place and Amenity.
    Please see below more detail: place_amenity in the Place update
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """Amenities class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
