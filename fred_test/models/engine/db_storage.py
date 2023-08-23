#!/usr/bin/python3
"""This module defines a class to manage sqldb storage for hbnb clone
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None
    __envs = {
        'env': os.getenv('HBNB_ENV'),
        'user': os.getenv('HBNB_MYSQL_USER'),
        'password': os.getenv('HBNB_MYSQL_PWD'),
        'host': os.getenv('HBNB_MYSQL_HOST'),
        'database': os.getenv('HBNB_MYSQL_DB')
        }

    def __init__(self):
        """instantiates new DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(DBStorage.__envs['user'],
                                   DBStorage.__envs['password'],
                                   DBStorage.__envs['host'],
                                   DBStorage.__envs['database']),
                                   pool_pre_ping=True)

    def all(self, cls=None):
        """queries on the current database session (self.__session) all
        objectsdepending of the class name"""
        session_objs = {}
        classes = self.__session.query(cls).all()
        for obj in classes:
            key = '{}.{}'.format(obj.__class__.name, obj.id)
            session_objs[key] = obj

        return session_objs

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """reloads the DBStorage"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
     
