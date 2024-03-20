#!/usr/bin/python3
""" New class for sqlalchemy. """
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    """ Creates tables in an environment. """
    __engine = None
    __session = None
    
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = gettenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host,db), pool_pre_ping=True)
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """ Returns a dictionary. """        
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls) 
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic.key = elem
        return (dic)      
    
    def new(self, obj):
        """ Add a new element in the table. """      
        self.__session.add(obj)
        
    def save(self):
        """ Saves changes. """
        self.__session.commit()
        
    def delete(self, obj=None):
        """ Deletes an element in the table. """
        if obj:
            self.session.delete(obj)
            
    def reload(self):
        """ Configuaration """                
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commiit=False)
        Session = scoped_session(sec)
        self.__session = Session()
    
    def close(self):
        """ Calls remove() function. """    
        self.__session.close()