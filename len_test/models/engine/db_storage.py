#!/usr/bin/python3
"""A new engine for DBStorage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship


class DBStorage():
    """a class for the database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for the class"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        # drop all tables if the environment variable is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all data from the database"""
        new = {}
        classes = {"State": State, "City": City, "User": User,
                   "Place": Place, "Review": Review, "Amenity": Amenity}
        if cls:
            if type(cls) == str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    new[key] = obj
            elif cls.__name__ in classes:
                for obj in self.__session.query(cls).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    new[key] = obj

        else:
            for key, value in classes.items():
                for obj in self.__session.query(value).all():
                    key = str(value.__name__) + "." + str(obj.id)
                    new[key] = obj

        return new

    def new(self, obj):
        """add object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in database and also a session"""
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)

        Session = scoped_session(session)
        self.__session = Session()
