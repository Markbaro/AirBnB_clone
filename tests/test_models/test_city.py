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
        instance = City(state_id="KEN", name="Kisumu")
        self.assertEqual(instance.state_id, "KEN")
        self.assertEqual(instance.name, "Kisumu")

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_city_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(City().__class__, BaseModel), True)

    def test_city_id(self):
        """tests the type of a City instance id"""
        self.assertEqual(str, type(City().id))

    def test_city_for_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_city_instantiation_no_args(self):
        """Tests the City instantiation with no parameters"""
        self.assertEqual(City, type(City()))

    def test_city_instance_id_is_unique(self):
        """test that the City instances ids are unique"""
        self.assertNotEqual(City().id, City().id)

    def test_city_created_at_is_datetime(self):
        """test datetime in City attribute created_at"""
        self.assertEqual(datetime, type(City().created_at))

    def test_city_updated_at_is_datetime(self):
        """test datetime in City attribute updated_at"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_name_attr_is_public_class_attr(self):
        """test that the City attribute name is public class attribute"""
        model = City()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(model))

    def test_city_created_at_attrs_are_different(self):
        """tests that the City created_at attributes for two
            instances are different"""
        self.assertLess(City().created_at, City().created_at)

    def test_city_updated_at_attrs_are_different(self):
        """tests that the City updated_at attribute for two
            instances are different"""
        self.assertLess(City().updated_at, City().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = City(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_city_instantiation_with_kwargs(self):
        "tests the instantiation of the City class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = City(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_city_instantiation_with_None_kwargs(self):
        """test User instatiation with a dictionary whose values are None"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_city_save_method_once(self):
        model = City()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_city_save_method_twice(self):
        model = City()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_city_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = City()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_city_save_to_update_file(self):
        model = City()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_city_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_city_to_dict_has_valid_keys(self):
        model = City()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

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
