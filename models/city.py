#!/usr/bin/python3
""" City Module """

from models.base_model import BaseModel


class City(BaseModel):
    """ Definition for class City """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init for instance of City """
        super().__init__(*args, **kwargs)
