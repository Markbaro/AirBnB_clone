#!/usr/bin/python3
"""Defines all unittest tests for the console.py module"""

import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittest for the HBNBCommand class"""

    missing_class = "** class name missing **"
    invalid_class = "** class doesn't exist **"
    unknown_syntax = "*** Unknown syntax: {}"
    missing_id = "** instance id missing **"
    missing_instance = "** no instance found **"

    def test_console_prompt(self):
        """test for the command line prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_cmd_line(self):
        """test for an empty command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertFalse("", f.getvalue().strip())

    def test_console_quit_cmd(self):
        """tests quit command"""
        with patch("sys.stdout", new=StringIO) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_console_EOF_cmd(self):
        """tests ctrl+d quit command"""
        with patch("sys.stdout", new=StringIO) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_empty_line(self):
        """Test empty lines are ignored by parser and not printed on stdout."""
        input = "   \n\t  \r\n     \n\t  \
        \r\n"
        expected_output = ""
        with patch("sys.stdout", new=StringIO()) as fakeOut:
            HBNBCommand().onecmd(input)
            output = fakeOut.getvalue().strip("\n")
            self.assertEqual(expected_output, output)

        with patch("builtins.print") as mock_print:
            cmd = HBNBCommand()
            cmd.emptyline()
            mock_print.assert_not_called()

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_console_create_cmd_with_missing_class(self):
        """tests the console create command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(
                TestHBNBCommand.missing_class,
                f.getvalue().strip()
            )

    def test_console_create_cmd_for_BaseModel_class(self):
        """tests the create cmd for the BaseModel class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'BaseModel.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_user_class(self):
        """tests the create cmd for the User class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'User.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_State_class(self):
        """tests the create cmd for the State class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'State.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_City_class(self):
        """tests the create cmd for the City class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'City.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_Amenity_class(self):
        """tests the create cmd for the Amenity class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'Amenity.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_Place_class(self):
        """tests the create cmd for the Place class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'Place.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_for_Review_class(self):
        """tests the create cmd for the Review class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(f.getvalue().strip()))
            key_id = f'Review.{f.getvalue().strip()}'
            self.assertIn(key_id, storage.all().keys())

    def test_console_create_cmd_with_invalid_class(self):
        """tests the console create command with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(
                TestHBNBCommand.invalid_class,
                f.getvalue().strip()
            )

    def test_console_create_cmd_with_invalid_syntax(self):
        """tests the console create command with invalid syntax"""
        cmd = 'MyModel.create()'
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(
                TestHBNBCommand.unknown_syntax.format(cmd),
                f.getvalue().strip()
            )
        cmd = 'Amenity.create()'
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(cmd))

    def test_console_show_cmd_for_BaseModel_class(self):
        """tests the show cmd for the BaseModel class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'BaseModel.{key_id}']
            cmd = f"show BaseModel {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_User_class(self):
        """tests the show cmd for the User class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'User.{key_id}']
            cmd = f"show User {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_State_class(self):
        """tests the show cmd for the State class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'State.{key_id}']
            cmd = f"show State {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_City_class(self):
        """tests the show cmd for the City class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'City.{key_id}']
            cmd = f"show City {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Amenity_class(self):
        """tests the show cmd for the Amenity class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Amenity.{key_id}']
            cmd = f"show Amenity {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Place_class(self):
        """tests the show cmd for the Place class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Place.{key_id}']
            cmd = f"show Place {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Review_class(self):
        """tests the show cmd for the Review class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Review.{key_id}']
            cmd = f"show Review {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_BaseModel_class_with_missing_id(self):
        """tests the show cmd for the BaseModel class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_User_class_with_missing_id(self):
        """tests the show cmd for the BaseModel class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_State_class_with_missing_id(self):
        """tests the show cmd for the State class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_City_class_with_missing_id(self):
        """tests the show cmd for the City class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_Amenity_class_with_missing_id(self):
        """tests the show cmd for the Amenity class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_Place_class_with_missing_id(self):
        """tests the show cmd for the Place class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_Review_class_with_missing_id(self):
        """tests the show cmd for the Review class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_show_cmd_for_BaseModel_class_with_invalid_id(self):
        """tests the show cmd for the BaseModel class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_User_class_with_invalid_id(self):
        """tests the show cmd for the User class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_State_class_with_invalid_id(self):
        """tests the show cmd for the State class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_City_class_with_invalid_id(self):
        """tests the show cmd for the City class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_Amenity_class_with_invalid_id(self):
        """tests the show cmd for the Amenity class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_Place_class_with_invalid_id(self):
        """tests the show cmd for the Place class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_show_cmd_for_Review_class_with_invalid_id(self):
        """tests the show cmd for the Review class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_BaseModel_class_with_missing_id(self):
        """tests the show desroy for the BaseModel class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_User_class_with_missing_id(self):
        """tests the destroy cmd for the BaseModel class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_State_class_with_missing_id(self):
        """tests the destroy cmd for the State class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_City_class_with_missing_id(self):
        """tests the destroy cmd for the City class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_Amenity_class_with_missing_id(self):
        """tests the destroy cmd for the Amenity class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_Place_class_with_missing_id(self):
        """tests the destroy cmd for the Place class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destoy_cmd_for_Review_class_with_missing_id(self):
        """tests the destoy cmd for the Review class with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(TestHBNBCommand.missing_id, f.getvalue().strip())

    def test_console_destroy_cmd_for_BaseModel_class_with_invalid_id(self):
        """tests the destroy cmd for the BaseModel class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                HBNBCommand().onecmd("destroy BaseModel 12121212")
            )
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_User_class_with_invalid_id(self):
        """tests the destroy cmd for the User class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_State_class_with_invalid_id(self):
        """tests the destroy cmd for the State class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_City_class_with_invalid_id(self):
        """tests the destroy cmd for the City class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_Amenity_class_with_invalid_id(self):
        """tests the destroy cmd for the Amenity class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_Place_class_with_invalid_id(self):
        """tests the destroy cmd for the Place class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_Review_class_with_invalid_id(self):
        """tests the destroy cmd for the Review class with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 12121212"))
            self.assertEqual(
                TestHBNBCommand.missing_instance,
                f.getvalue().strip()
            )

    def test_console_destroy_cmd_for_BaseModel_class(self):
        """tests the destroy cmd for the BaseModel class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'BaseModel.{key_id}']
            cmd = f"destroy BaseModel {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(found, storage.all())

    def test_console_show_cmd_for_User_class(self):
        """tests the show cmd for the User class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'User.{key_id}']
            cmd = f"show User {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_State_class(self):
        """tests the show cmd for the State class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'State.{key_id}']
            cmd = f"show State {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_City_class(self):
        """tests the show cmd for the City class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'City.{key_id}']
            cmd = f"show City {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Amenity_class(self):
        """tests the show cmd for the Amenity class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Amenity.{key_id}']
            cmd = f"show Amenity {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Place_class(self):
        """tests the show cmd for the Place class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Place.{key_id}']
            cmd = f"show Place {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())

    def test_console_show_cmd_for_Review_class(self):
        """tests the show cmd for the Review class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            key_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            found = storage.all()[f'Review.{key_id}']
            cmd = f"show Review {key_id}"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(found.__str__(), f.getvalue().strip())
