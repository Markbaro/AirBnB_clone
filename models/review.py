#!/usr/bin/python3
"""Defines the Review model class, a subclass of BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class is a subclass of the BaseModel class
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty sting
    """
    place_id = ''
    user_id = ''
    text = ''
