#!/usr/bin/python3
""" Test cases for Review Module """
import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Tests methods for Review """
    def test_review_instance(self):
        """ create new instance """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_args(self):
        """ test args with review instance """
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))


if __name__ == "__main__":
    unittest.main()
