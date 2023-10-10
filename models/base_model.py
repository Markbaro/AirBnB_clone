#!/usr/bin/python3
"""
Module defines the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class defines all available attributes
    and Methods for all subclasses and instances
    """
    pass

    def __init__(self, *args, **kwargs):
        """
        BaseModel method that initializes all public instances
            1.i.d
            2.created_at
            3.updated_at
        """
        pass

    def __str__(self):
        """
        Overriding the toString method
        """
        pass

    def save(self):
        """
        Sets the updated_at public instance attribute
        to the current date and time
        """
        pass

    def to_dict(self):
        """
        Creates a dictionary from all the key-value pairs in
        the __dict__ attribute of the current BaseModel instance
        """
        pass
