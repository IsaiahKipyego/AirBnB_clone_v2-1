#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=True)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """getter attribute for reviews"""
            review_list = []
            for review in self.reviews:
                if review.place_id == Place.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            """getter for the amenities"""
            amenities = []
            for a_id in self.amenity_ids:
                key = 'Amenity.' + a_id
                if key in FileStorage.__objects:
                    amenities.append(FileStorage.__objects[key])

            return amenities

        @amenities.setter
        def amenities(self, value):
            """setter function for the amenities available"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
