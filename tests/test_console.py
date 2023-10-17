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





