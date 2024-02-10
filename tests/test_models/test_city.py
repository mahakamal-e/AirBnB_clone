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
        city.name = "Ali"
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

    def test_str_method(self):
        """ Test case for __str__ method """
        city = City()
        n = city.__class__.__name__
        result_str = f"[{n}] ({city.id}) <{city.__dict__}>"
        self.assertEqual(city.__str__(), result_str)

if __name__ == "__main__":
    unittest.main()