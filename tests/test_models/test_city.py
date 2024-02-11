#!/usr/bin/python3
""" Test cases for City module"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestCityMethods(unittest.TestCase):
    """ Test cases """
    def setUp(self):
        """ Method that calls befor each test case """
        city = City()
        city.name = "Maha"
        city.id = "123-123-123"

    def test_type_class(self):
        """ Test for type of class """
        self.assertEqual(City, type(City()))

    def test_unique_ids(self):
        """ Test id """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_typeParent_class(self):
        """ Test Type of parent class """
        self.assertIsInstance(City(), BaseModel)

    def test_init_method(self):
        """ Test cases for attr """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_str_representation(self):
        """Test __str__ method for correct string representation"""
        instance = City(id='123', name='example', value=42)
        exr = "[City] (123) {'id': '123', 'name': 'example', 'value': 42}"
        self.assertEqual(str(instance), exr_str)


if __name__ == "__main__":
    unittest.main()
