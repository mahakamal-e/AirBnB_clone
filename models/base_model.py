#!/usr/bin/python3
""" Base Model Module for all models"""

import uuid
from datetime import datetime, date
import models


class BaseModel:
    """
    Main class used defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for the class automatically called,
        when an object is created from a class.
        Args:
           args: number of arguments.
           kwargs: number of kwargs key pair arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ["updated_at", "created_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)

    def save(self):
        """ Method used to updates the public instance attribute updated_at,
        with the current datetime. """
        updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ Method that return string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self) -> dict:
        """ Method used to return a dictionary all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
