#!/usr/bin/python3
""" File storage module """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Class that used to serializes instances to a JSON file,
    and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        Method that  sets in __objects the obj,
        with key <obj class name>.id

        Args:
           obj: obj will be set.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Method that serializes __objects to the JSON file (path: __file_path)
        """
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as file_:
            json.dump(objects_dict, file_)

    def reload(self):
        """ Method that deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file_:
                create_dict = json.load(file_)
                for key, value in create_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
