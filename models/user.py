#!/usr/bin/python3
""" User Module """

from models.base_model import BaseModel


class User(BaseModel):
    """ Definition of a class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
