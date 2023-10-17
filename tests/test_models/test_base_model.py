#!/usr/bin/python3
"""Defines unnittest tests for the superclass BaseModel"""

import unittest
import os
import models
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest tests for the BaseModel model class"""

    instance1 = ""

    def test_base_model_instance_stored(self):
        """Tests that a new BaseModel instance is stored"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_base_model_id(self):
        """tests the type of a BaseModel instance id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_base_model_created_at_is_datetime(self):
        """test datetime in BaseModel class attribute created_at"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_base_model_instance_id_is_unique(self):
        """test that the BaseModel instances ids are unique"""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_base_model_created_at_attr_are_different(self):
        """tests that the BaseModel created_at attributes for two
            instances are different"""
        self.assertLess(BaseModel().created_at, BaseModel().created_at)

    def test_base_model_updated_at_attr_are_different(self):
        """tests that the BaseModel updated_at attribute for two
            instances are different"""
        self.assertLess(BaseModel().updated_at, BaseModel().updated_at)

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

    def test_save(self):
        """Test save method updates the updated_at.

        And that updated_at is at a later time than created at
        """
        self.instance1 = BaseModel()
        self.instance1.save()
        self.assertNotEqual(
            self.instance1.created_at, self.instance1.updated_at)
        self.assertGreater(
            self.instance1.updated_at, self.instance1.created_at)

    def test_base_model_updated_at_is_datetime(self):
        """test datetime in BaseModel class attribute updated_at"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_to_dict(self):
        """Test if the dict representation contains all keys"""
        self.instance1 = BaseModel()
        # Checks that all the keys were created
        expectedKeys = ["id", "created_at", "updated_at"]
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertTrue((key in list(actualDict)))
        # Checks that the method returns a dictionary
        self.assertIsInstance(self.instance1.to_dict(), dict)
        # cheks for correct type(str) for each key
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertIsInstance(self.instance1.to_dict()[key], str)
        # Checks that the key:values match the instances
        instance_dict = self.instance1.to_dict()
        self.assertEqual(instance_dict["id"], self.instance1.id)
        self.assertEqual(
            instance_dict["created_at"], self.instance1.created_at.isoformat()
        )
        self.assertEqual(
            instance_dict["updated_at"], self.instance1.updated_at.isoformat()
        )


if __name__ == '__main__':
    unittest.main()
