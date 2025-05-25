#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """Class for places"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Relationship
    reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns list of Review instances with place_id == self.id"""
            from models import storage
            from models.review import Review
            return [review for review in storage.all(Review).values() if review.place_id == self.id]
