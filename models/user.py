#!/usr/bin/python3
"""User module: inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class: public class attributes."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
