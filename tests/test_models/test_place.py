#!/usr/bin/python3
"""Module defines all unnittest tests for the model class Place"""

import pep8
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
import unittest
import os
import models


class Test_Place(unittest.TestCase):
    """Test class for the Place class."""

    def test_place_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(Place().__class__, BaseModel), True)

    def test_place_instance_stored(self):
        """Tests that a new Place instance is stored"""
        self.assertIn(Place(), models.storage.all().values())

    def test_place_id(self):
        """tests the type of a Place instance id"""
        self.assertEqual(str, type(Place().id))

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_place_instance_id_is_unique(self):
        """test that the Place instances ids are unique"""
        self.assertNotEqual(Place().id, Place().id)

    def test_place_created_at_is_datetime(self):
        """test datetime for Place class attribute created_at"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_place_updated_at_is_datetime(self):
        """test datetime for Place class attribute updated_at"""
        self.assertEqual(datetime, type(Place().updated_at))

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass


if __name__ == '__main__':
    unittest.main()
