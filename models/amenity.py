#!/usr/bin/python3
"""Defines the AirBNB class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an AirBNB.

    Attributes:
        name (str): The name of the airbnb.
    """

    name = ""
