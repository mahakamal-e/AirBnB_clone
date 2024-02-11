#!/usr/bin/python3
""" Unittests for command console module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """ Test cases for console command """
    def setUp(self):
        """ Method that calls before every test """
        self.console = HBNBCommand()

    def test_help_command(self):
        """the help command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("help", output)
            self.assertIn("EOF", output)

    def test_quit_command(self):
        """ quit command exits test with patch """
        result = self.console.onecmd("quit")
        self.assertTrue(result)

    def test_emptyline_method(self):
        """the emptyline method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("any command")
            self.assertEqual("", f.getvalue())

    def test_create_command(self):
        """command create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_count_command(self):
        """the count command """
        count = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                count += 1
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, str(count))

    def test_show_command(self):
        """ show command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** no instance found **")

    def test_destroy_command(self):
        """destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** no instance found **")

    def test_all_command(self):
        """Test to check the all command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_update_command(self):
        """update command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'basemodel'")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")
            self.assertNotEqual(output, "** instance id missing **")
            self.assertNotEqual(output, "** attribute name missing **")
            self.assertNotEqual(output, "** value missing **")
            self.assertNotEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
