#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

# load from database
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()

else:  # load from filestorage
    from models.engine.file_storage import FileStorage

    storage = FileStorage()

storage.reload()
