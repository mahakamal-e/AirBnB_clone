#!/usr/bin/python3
""" Test cases for User Module """

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestUserMethods(unittest.TestCase):
    """ Test cases for User """
    def test_userInstanceType(self):
        """Test the type of instance """
        self.assertEqual(User, type(User()))

    def Test_userParent(self):
        """ Test User Inhertance from BaseModel or not """
        self.assertIsInstance(User(), BaseModel)

    def test_initialization(self):
        """ test cases for init """
        user_info = {
            'id': '445',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000',
            'email': 'test_@example.com',
            'password': 'secure_pass',
            'first_name': 'Maha',
            'last_name': 'Kamal'
            }
        user = User(**user_info)
        self.assertEqual(user.id, '445')
        self.assertEqual(user.email, 'test_@example.com')
        self.assertEqual(user.password, 'secure_pass')
        self.assertEqual(user.first_name, 'Maha')
        self.assertEqual(user.last_name, 'Kamal')

    def test_createInstance_withoutKwargs(self):
        """ Test Instamce with args only """
        user = User()
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_email_value(self):
        """Test email value empty """
        user = User()
        self.assertEqual(user.email, "")

    def test_email_type(self):
        """ Test email value type str"""
        user = User()
        self.assertEqual(str, type(User().email))

    def test_user_id(self):
        """Test type of user id"""
        user = User()
        self.assertIsInstance(user.id, str)

    def test_created_at(self):
        """Test type of user created_at type (datatime) """
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_update_at(self):
        """ Test typr of updated_at type """
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_str_method(self):
        """ Test method for __str__ method print string reeprsentation """
        user = User()
        name_class = user.__class__.__name__
        expected_str = f"[{name_class}] ({user.id}) {user.__dict__}"
        self.assertEqual(user.__str__(), expected_str)

    def test_to_dict_method(self):
        """ Test to_dict method from BaseModel class"""
        user = User()
        to_dict_ = user.to_dict()
        new_dict = user.__dict__.copy()
        new_dict["__class__"] = user.__class__.__name__
        new_dict["updated_at"] = user.updated_at.isoformat()
        new_dict["created_at"] = user.created_at.isoformat()
        self.assertDictEqual(new_dict, to_dict_)


if __name__ == "__main__":
    unittest.main()