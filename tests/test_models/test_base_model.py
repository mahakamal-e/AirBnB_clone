#!/usr/bin/python3
""" Test cases for BaseModel class. """

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ class used to creat testcases """
    def setUp(self):
        """ method called before each test """
        pass

    def tearDown(self):
        """ method called after each test """
        pass

    def test_instance(self):
        """ test type of class """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_notNone(self):
        """ test id"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)

    def test_instance_attributes(self):
        """ test init method with args """
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89
        self.assertEqual(obj.name, "My First Model")
        self.assertEqual(obj.my_number, 89)

    def test_instance_kwargs(self):
        """Test init method with kwargs"""
        base = BaseModel()
        base.name = "My First Model"
        base.my_number = 89
        my_base_json = base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 89)
        self.assertNotEqual(new_base, base)
        self.assertDictEqual(new_base.__dict__, base.__dict__)

    def test_save_idTest(self):
        """test cases for save method"""
        base = BaseModel()
        id_ = base.id
        base.save()
        self.assertEqual(base.id, id_)

    def test_save_testUpdate_at(self):
        """test cases for save method"""
        base = BaseModel()
        original_updated_at = base.updated_at
        base.save()
        self.assertEqual(original_updated_at, base.updated_at)

    def test_save_testArg(self):
        """test cases for save method"""
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_to_dict_type(self):
        """ Test cases for to_dict method """
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_to_dict_changingId(self):
        """ Test cases for to_dict method """
        base = BaseModel()
        base.name = "Maha"
        self.assertIn("Maha", base.to_dict().values())

    def test_to_dict_(self):
        """ Test cases for to_dict method """
        obj = BaseModel()
        to_dict_returned_dict = obj.to_dict()
        expected_dic = obj.__dict__.copy()
        expected_dic["__class__"] = obj.__class__.__name__
        expected_dic["updated_at"] = obj.updated_at.isoformat()
        expected_dic["created_at"] = obj.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_str_method(self):
        """ Test cases for str method """
        base = BaseModel()
        str_obj = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base.__str__(), str_obj)


if __name__ == '__main__':
    unittest.main()
