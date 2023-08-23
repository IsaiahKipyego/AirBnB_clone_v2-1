#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import os


class test_Amenity(test_basemodel):
    """Amenity class tests"""

    @classmethod
    def setUpClass(cls):
        """Sets up test class"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """destroys test class"""
        try:
            os.remove("file.json")
            del cls.amenity
        except Exception as ex:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_attributes(self):
        """checks amenity attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)

    def test_save(self):
        """tests save functionality"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_attribute_types(self):
        """tests attribute type"""
        self.assertEqual(type(self.amenity.name), str)
        self.assertEqual(type(self.amenity.id), str)

    def test_inheritance(self):
        """test if is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
