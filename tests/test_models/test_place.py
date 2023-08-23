#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()
        cls.place.city_id = "3781254d-2b6d-4638-9237-ac59b11763b3"
        cls.place.user_id = "dae79fb8-0580-441f-929a-788697e809dd"
        cls.place.name = "My House"
        cls.place.description = "You're always welcome"
        cls.place.number_rooms = 7
        cls.place.number_bathrooms = 4
        cls.place.max_guest = 100
        cls.place.price_by_night = 100
        cls.place.latitude = 1323.344
        cls.place.longitude = -1100.3299
        cls.place.amenity_ids = ["c1ea62e2-6e79-46da-9d46-597f4d7cecd0"]

    def __init__(self, *args, **kwargs):
        """test init"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
