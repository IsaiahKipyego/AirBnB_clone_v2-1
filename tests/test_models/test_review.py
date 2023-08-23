#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.review import Review
import unittest
import os
from os import getenv

class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
    @classmethod
    def setUpClass(cls):
        """test"""
        cls.review = Review()
        cls.review.place_id = "3781254d-2b6d"
        cls.review.user_id = "9237-ac59b11763b3"
        cls.review.text = "The best i ever had..."

    @classmethod
    def teardown(cls):
        """tears down test"""
        del cls.review

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_checking_doc(self):
        """test doc"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """checks attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_is_subclass(self):
        """test if review is subclass of the BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save(self):
        """test save"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """test dictionary"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
