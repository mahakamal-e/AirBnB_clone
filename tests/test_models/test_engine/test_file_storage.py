#!/usr/bin/python3
""" Test Module for class FileStorage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """ Test Cases """
    def setUp(self):
        """ Method that calls after echa test case """
        self.file_path = "file_test.json"
        self.__file_path = self.file_path

    def tearDown(self):
        """ Method that calls after each test """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_fileStorage_type(self):
        """ test type of file storage class """
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_fileStorage_init_with_args(self):
        """ Test case call class with args """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_file_path(self):
        """Test that __file_path is a private string attribute"""
        f_storage = FileStorage()
        with self.assertRaises(AttributeError):
            f_storage.__file_path

    def test_file_storage_objects(self):
        """Test that __objects is a private dictionary attribute"""
        f_storage = FileStorage()
        with self.assertRaises(AttributeError):
            f_storage.__objects

    def test_all_method(self):
        """ Test cases for all method """
        self.assertEqual(dict, type(FileStorage().all()))

    def test_all_args(self):
        """ Test cases for all method """
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_save_method(self):
        """ Test cases save method """
        f_storage = FileStorage()
        test_obj = BaseModel()
        f_storage.new(test_obj)
        f_storage.save()


if __name__ == "__main__":
    unittest.main()
