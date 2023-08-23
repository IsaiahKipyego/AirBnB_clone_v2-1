#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place


classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

# load from database
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()

else:  # load from filestorage
    from models.engine.file_storage import FileStorage

    storage = FileStorage()

storage.reload()
