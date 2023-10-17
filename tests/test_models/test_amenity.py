#!/usr/bin/python3
"""This module defines unit tests for the Amenity class."""

import unittest
import os
import models
import pep8
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Test class for the Amenity class."""

    def test_instance_creation(self):
        """Test if an instance of Amenity is created successfully."""
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes."""
        instance = Amenity(name="WiFi")
        self.assertEqual(instance.name, "WiFi")

    def test_amenity_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(Amenity().__class__, BaseModel), True)

    def test_amenity_instance_id_is_unique(self):
        """test that the Amenity instances ids are unique"""
        self.assertNotEqual(Amenity().id, Amenity().id)

    def test_amenity_instance_stored(self):
        """Tests that a new Amenity instance is stored"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_amenity_id(self):
        """tests the type of a Amenity instance id"""
        self.assertEqual(str, type(Amenity().id))

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

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

    def test_amenity_created_at_is_datetime(self):
        """test datetime in Amenity attribute created_at"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_amenity_updated_at_is_datetime(self):
        """test datetime in Amenity attribute updated_at"""
        self.assertEqual(datetime, type(Amenity().updated_at))


if __name__ == '__main__':
    unittest.main()
