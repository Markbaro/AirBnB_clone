#!/usr/bin/python3
"""Module defines unit tests for the City class."""

import pep8
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import unittest
import os
import models


class Test_City(unittest.TestCase):
    """Test class for the City class."""

    def test_instance_creation(self):
        """Test if an instance of City is created successfully."""
        instance = City()
        self.assertIsInstance(instance, City)

    def test_city_attributes(self):
        """Test City attributes."""
        instance = City(state_id="KENYA", name="Kisumu")
        self.assertEqual(instance.state_id, "KEN")
        self.assertEqual(instance.name, "Kisumu")

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_city_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(City().__class__, BaseModel), True)

    def test_city_instance_stored(self):
        """Tests for new City instance is stored"""
        self.assertIn(City(), models.storage.all().values())

    def test_city_id(self):
        """tests the type of a City instance id"""
        self.assertEqual(str, type(City().id))

    def test_city_instance_id_is_unique(self):
        """test that the City instances ids are unique"""
        self.assertNotEqual(City().id, City().id)

    def test_city_created_at_is_datetime(self):
        """test datetime in City attribute created_at"""
        self.assertEqual(datetime, type(City().created_at))

    def test_city_updated_at_is_datetime(self):
        """test datetime in City attribute updated_at"""
        self.assertEqual(datetime, type(City().updated_at))

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
