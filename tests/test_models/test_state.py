#!/usr/bin/python3
""" Test cases for State Module """
import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test cases for state """
    def test_state_instance(self):
        """ test creat instance from class State"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_args(self):
        """ test cases for args with State instance """
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))


if __name__ == "__main__":
    unittest.main()
