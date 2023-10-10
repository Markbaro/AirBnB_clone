#!/usr/bin/python3
"""Module defines class City a subclass of the BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City is a subclass of the BaseModel class public class attributes
        a) state_id: string - empty string: it will be the State.id
        b) name:string - empty string
    """
    
    state_id = ''
    name = ''