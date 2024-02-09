#!/usr/bin/python3
""" State Module """

from models.base_model import BaseModel


class State(BaseModel):
    """ Definition of class State that inheirts from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """init (constractor) for instance of State"""
        super().__init__(*args, **kwargs)
