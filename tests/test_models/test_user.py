#!/usr/bin/python3
"""Module defines unit tests for the User class."""

import unittest
import os
import models
import pep8
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """Test cases for the User class"""

    instance = ""

    def test_user_attributes(self):
        """Test Class User attributes."""
        self.assertEqual(self.instance.email, "user@example.com")
        self.assertEqual(self.instance.password, "secretpassword01")
        self.assertEqual(self.instance.first_name, "Ada")
        self.assertEqual(self.instance.last_name, "Alice")

    def test_pep_style(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_user_as_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(User().__class__, BaseModel), True)

    def test_instance_creation(self):
        """Test if user instance is created successfully."""
        self.assertIsInstance(self.instance, User)

    def test_user_to_dict_and_magic_dict_methods(self):
        model = User()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_user_to_dict_method_with_None_arg(self):
        model = User()
        with self.assertRaises(TypeError):
            model.to_dict(None)

    def test_user_created_at(self):
        """test datetime for User attribute created_at"""
        self.assertEqual(datetime, type(User().created_at))

    def test_user_for_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_user_name_attr_is_public_class_attr(self):
        """test that the User attribute name is public class attribute"""
        model = User()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(model))

    def test_user_instantiation_no_args(self):
        """Tests the User instantiation with no parameters"""
        self.assertEqual(User, type(User()))

    def test_user_created_at_attr_are_different(self):
        """tests that the User created_at attributes for two
            instances are different"""
        self.assertLess(User().created_at, User().created_at)

    def test_user_updated_at_attr_are_different(self):
        """tests that the User updated_at attribute for two
            instances are different"""
        self.assertLess(User().updated_at, User().updated_at)

    def test_user_updated_at(self):
        """test datetime of User attribute updated_at"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_user_instance_id_is_unique_instance_id(self):
        """test User instances ids are unique"""
        self.assertNotEqual(User().id, User().id)

    @classmethod
    def setUpClass(cls) -> None:
        """This method is called once before any tests are run"""
        cls.instances = []

    @classmethod
    def tearDownClass(cls) -> None:
        """This method is called once after all tests are run"""
        cls.instances.clear()

    def setUp(self) -> None:
        """Call b4 each test case to set up the initial state."""
        self.instance = User(
            email="user@example.com",
            password="secretpassword01",
            first_name="Ada",
            last_name="Alice",
        )
        # return super().setUp()

    def tearDown(self) -> None:
        """This method is called after each test method is run """
        del self.instance
        self.instances.clear()


if __name__ == '__main__':
    unittest.main()
