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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Converts the __objects dictionary
        to JSON and saves it to a file.
        """
        dump = {k: val.to_dict() for k, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(dump))

    def reload(self):
        """
        Loads the JSON file from __file_path and converts
        it to a Python dictionary.
        If the file does not exist, do nothing
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                payload = f.read()
            paydict = json.loads(payload)
            for key, val in paydict.items():
                classname, obj_id = key.split(".")
                cls = eval(classname)
                FileStorage.__objects[key] = cls(**val)
