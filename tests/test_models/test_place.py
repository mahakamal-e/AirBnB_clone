#!/usr/bin/python3
""" Test cases for Place Module """

import unittest
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """ unittests for class Place """
    def test_place_instance(self):
        """ Create new instance from Place """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_args(self):
        """ test cases for input args"""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))


if __name__ == "__main__":
    unittest.main()
