#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os
from models import BaseModel
import unittest


class test_state(test_basemodel):
    """ tests state class"""
    @classmethod
    def setUpClass(cls):
        """set up test"""
        cls.state = State()
        cls.state.name = "LA"

    @classmethod
    def teardown(cls):
        """delete class"""
        del cls.state

    def tearDown(self):
        """teardown test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_doc(self):
        """test doc"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """checks attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass(self):
        """test if state is subclass of the BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types(self):
        """test attribute"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """test save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """test dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
