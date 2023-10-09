#!/usr/bin/python3
"""Module defines class User which is a subclass of BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User is a subclass of the BaseModel class with the public class attributes
        a. email: string - empty string
        b. password: string - empty string
        c. first_name: string - empty string
        d. last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''