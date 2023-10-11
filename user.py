#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Creating new Instance--")
my_state = State()
my_state.name = "Kenya"
my_city = City()
my_city.name = "Nairobi"
my_amenity = Amenity()
my_amenity.name = "adventure park"
my_place = Place()
my_place.name = "nairobi city park"
my_place.description = "animal park with the big 5"
my_place.price = "$100"
my_place.number_rooms = 2
my_place.max_guests = 10
my_place.latitude = 1.46
my_place.longitude = 1.34
my_review = Review()
my_review.text = "what a lively place!"

my_state.save()
my_city.save()
my_amenity.save()
my_place.save()
my_review.save()
print(my_state)
print(my_city)
print(my_amenity)
print(my_place)
print(my_review)