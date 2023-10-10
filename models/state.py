#!/usr/bin/python3
"""Module defines class State which is a subclass of the BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    The class is a subclass of the BaseModel class with the
        additional public class attributes defined
        a) name: string-empty string
    """
    name = ''