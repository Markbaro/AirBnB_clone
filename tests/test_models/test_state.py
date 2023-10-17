#!/usr/bin/python3
"""Defines unnittest tests for the state module"""

import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
import unittest
import os
import models


class Test_State(unittest.TestCase):
    """Test class for the State class"""

    def test_instance_creation(self):
        """Test if instance of State is created successfully."""
        instance = State()
        self.assertIsInstance(instance, State)

    def test_state_attributes(self):
        """Test State attributes."""
        instance = State(name="Kenya")
        self.assertEqual(instance.name, "Kenya")

    def test_pycode_style(self):
        """Test for pycodePEP8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_state_as_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(State().__class__, BaseModel), True)

    def test_state_id(self):
        """tests the type of a State instance id"""
        self.assertEqual(str, type(State().id))

    def test_state_created_at_is_datetime(self):
        """test datetime of State attribute created_at"""
        self.assertEqual(datetime, type(State().created_at))

    def test_state_updated_at_is_datetime(self):
        """test datetime of State attribute updated_at"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_state_for_doc(self):
        self.assertIsNotNone(State.__doc__)

    def test_unused_args(self):
        """test for unused args"""
        model = State(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_state_instantiation_with_kwargs(self):
        "tests the instantiation of the State class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = State(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_state_created_at_attr_are_different(self):
        """tests that the State created_at attrs are different"""
        self.assertLess(State().created_at, State().created_at)

    def test_state_updated_at_attr_are_different(self):
        """tests that the State updated_at attrs are different"""
        self.assertLess(State().updated_at, State().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = State(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_state_name_attr_is_public_class_attr(self):
        """test that the Sate attribute name is public class attribute"""
        model = State()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(model))

    def test_state_instantiation_no_args(self):
        """Tests the State instantiation with no parameters"""
        self.assertEqual(State, type(State()))

    def test_state_instance_id_is_unique(self):
        """test that the State instances ids are unique"""
        self.assertNotEqual(State().id, State().id)

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
