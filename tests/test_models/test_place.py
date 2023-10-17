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

    def test_place_id(self):
        """tests the type of a Place instance id"""
        self.assertEqual(str, type(Place().id))

    def test_place_for_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_place_name_attr_is_public_class_attr(self):
        """test that the Place attribute name is public class attribute"""
        model = Place()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(model))

    def test_place_instantiation_no_args(self):
        """Tests the Place instantiation with no parameters"""
        self.assertEqual(Place, type(Place()))

    def test_place_created_at_is_datetime(self):
        """test datetime for Place class attribute created_at"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_place_updated_at_is_datetime(self):
        """test datetime for Place class attribute updated_at"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_name_attr_is_public_class_attr(self):
        """test that the Place attribute name is public class attribute"""
        model = Place()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(model))

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

    def test_place_to_dict_and_magic_dict_methods(self):
        model = Place()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_place_to_dict_method_with_None_arg(self):
        model = Place()
        with self.assertRaises(TypeError):
            model.to_dict(None)

    def test_place_save_method_once(self):
        model = Place()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_place_save_method_twice(self):
        model = Place()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_place_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = Place()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_place_save_to_update_file(self):
        model = Place()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

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

    def test_instance_creation(self):
        """Test if an instance of Place is created successfully."""
        instance = Place()
        self.assertIsInstance(instance, Place)

    def test_place_attributes(self):
        """Test Place attributes."""
        instance = Place(
            city_id="NBO",
            user_id="gabby_com",
            name="Penthouse Apartment",
            description="Beautiful apartment in the city",
            number_rooms=4,
            number_bathrooms=4,
            max_guest=6,
            price_by_night=350,
            latitude=17.7649,
            longitude=-172.9194,
            amenity_ids=["wifi", "Swimming Pool", "parking"],
        )
        self.assertEqual(instance.city_id, "NBO")
        self.assertEqual(instance.user_id, "gabby_com")
        self.assertEqual(instance.name, "Penthouse Apartment")
        self.assertEqual(instance.description,
                         "Beautiful apartment in the city")
        self.assertEqual(instance.number_rooms, 4)
        self.assertEqual(instance.number_bathrooms, 4)
        self.assertEqual(instance.max_guest, 6)
        self.assertEqual(instance.price_by_night, 350)
        self.assertEqual(instance.latitude, 17.7649)
        self.assertEqual(instance.longitude, -172.9194)
        self.assertEqual(instance.amenity_ids,
                         ["wifi", "Swimming Pool", "parking"])


if __name__ == '__main__':
    unittest.main()
