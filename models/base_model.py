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

    def __init__(self, *args, **kwargs):
        """
        BaseModel method that initializes all public instances
            1.i.d
            2.created_at
            3.updated_at
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Overriding the toString method
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Sets the updated_at public instance attribute
        to the current date and time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictionary from all the key-value pairs in
        the __dict__ attribute of the current BaseModel instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(__class__.__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return (my_dict)
