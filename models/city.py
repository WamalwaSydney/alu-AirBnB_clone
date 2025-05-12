#!/usr/bin/python3
"""City module: inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class: public class attributes."""
    state_id = ""
    name = ""
