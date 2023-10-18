#!/usr/bin/python3
"""This model contains unit tests for the FileStorage class."""

# import os
# import sys
import unittest
from unittest.mock import patch, mock_open, Mock
import json

# Import the classes and functions you want to test
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class Test_File_Storage(unittest.TestCase):
    def test_instance_creation(self):
        instance = FileStorage()
        self.assertIsInstance(instance, FileStorage)

    def test_attributes(self):
        instance = FileStorage()
        self.assertEqual(instance._FileStorage__file_path, "file.json")
        self.assertIsInstance(instance._FileStorage__objects, dict)

    def test_all_method(self):
        instance = FileStorage()
        all_objects = instance.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, instance._FileStorage__objects)

    def test_new_method(self):
        instance = FileStorage()
        obj = BaseModel()
        instance.new(obj)
        self.assertIn("BaseModel." + obj.id, instance._FileStorage__objects)

    """def test_save_method(self):
        m = mock_open()
        instance = FileStorage()
        obj = BaseModel()
        #obj.save = lambda: None
        instance.new(obj)
        with patch('builtins.open', m):
            instance.save()
            m.assert_called_once_with(instance._FileStorage__file_path,
            'w', encoding='utf-8')
            m().write.assert_called_once()"""

    def test_reload_method(self):
        instance = FileStorage()
        obj = BaseModel()
        obj_dict = obj.to_dict()
        with patch(
            "models.engine.file_storage.open",
            mock_open(read_data=json.dumps({"BaseModel." + obj.id: obj_dict})),
        ) as m:
            instance.reload()
            m.assert_called_once_with(
                instance._FileStorage__file_path, "r", encoding="utf-8"
            )
            self.assertIn("BaseModel." + obj.id,
                          instance._FileStorage__objects)
