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
    """
    Class for serialization and deserialization
    of instances to JSON
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Creates & returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores the object obj with the key <obj class name>.id
        in the __objects dictionary
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Converts the __objects dictionary
        to JSON and saves it to a file.
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        Loads the JSON file from __file_path and converts
        it to a Python dictionary.
        If the file does not exist, do nothing
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
