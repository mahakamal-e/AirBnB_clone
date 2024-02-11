#!/usr/bin/python3
""" test cases for Amenity"""

import unittest
import models
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ test amenity """

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_init_not_none(self):
        """Test instance not none"""
        self.assertIsNotNone(Amenity())

    def test_id_uuid(self):
        """ test is is str"""
        self.assertIsInstance(Amenity().id, str)

    def test_name(self):
        """ test name """
        name_ = self.value()
        self.assertEqual(type(name_.name), str)


if __name__ == "__main__":
    unittest.main()
