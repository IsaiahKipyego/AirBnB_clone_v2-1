#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import unittest
import os

class test_City(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        """sets  test class"""
        cls.city = City()
        cls.city.name = "Los Angeles"
        cls.city.state_id = "LA"

    @classmethod
    def teardown(cls):
        """tears down class attr"""
        del cls.city

    def tearDown(self):
        """destroys test class"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_attributes(self):
        """check city  attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_save(self):
        """tests save functionality"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_attribute_types(self):
        """tests attribute type"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.id), str)

    def test_inheritance(self):
        """test if is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
