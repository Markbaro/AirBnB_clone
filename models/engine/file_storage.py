#!/usr/bin/python3
"""
Defines the file_storage module
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    pass

    def all(self):
        """Creates & returns dictionary __objects"""
        pass

    def new(self, obj):
        """Stores the object obj with the key <obj class name>.id
        in the __objects dictionary
        """
        pass

    def save(self):
        """ Converts the __objects dictionary
        to JSON and saves it to a file.
        """
        pass

    def reload(self):
        """
        Loads the JSON file from __file_path and converts
        it to a Python dictionary.
        If the file does not exist, do nothing
        """
        pass
