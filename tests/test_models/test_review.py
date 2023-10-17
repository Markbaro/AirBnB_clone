#!/usr/bin/python3
"""Module defines unit tests for the Review class."""

import unittest
import os
import models
import pep8
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    """Test class for the Review class."""

    def test_instance_creation(self):
        """Test if an instance of Review is created successfully."""
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_review_attributes(self):
        """Test Review attributes."""
        instance = Review(
            place_id="Penthouse123",
            user_id="gabby_com",
            text="Great place to stay!"
        )
        self.assertEqual(instance.place_id, "Penthouse123")
        self.assertEqual(instance.user_id, "gabby_com")
        self.assertEqual(instance.text, "Great place to stay!")

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_review_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(Review().__class__, BaseModel), True)

    def test_review_instance_id_is_unique(self):
        """test that Review instances ids are unique"""
        self.assertNotEqual(Review().id, Review().id)

    def test_review_created_at_is_datetime(self):
        """test datetime Review class attribute created_at"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_updated_at_is_datetime(self):
        """test datetime for Review attribute updated_at"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_created_at_is_datetime(self):
        """test that the Review class attribute created_at is an instance
            of datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_updated_at_is_datetime(self):
        """test that the Review attribute updated_at is an
            instance of datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_name_attr_is_public_class_attr(self):
        """test that the Review class attribute,
            name is public class attribute"""
        model = Review()
        self.assertNotIn("name", model.__dict__)
        self.assertIn("id", dir(model))

    def test_review_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_review_instantiation_no_args(self):
        """Tests the Review instantiation with no parameters"""
        self.assertEqual(Review, type(Review()))

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

    def test_review_id(self):
        """tests the type of a Review instance id"""
        self.assertEqual(str, type(Review().id))


if __name__ == '__main__':
    unittest.main()
