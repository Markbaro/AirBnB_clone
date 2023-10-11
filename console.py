#!/usr/bin/python3
"""The module contains the HBNBCommand class"""


import cmd
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """
        Quit the command interpreter.
        """
        print("Goodbye!")
        return True

    def do_EOF(self, arg):
        """
        Quit the command interpreter on EOF.
        """
        print("exiting")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Create an object from the specified class."""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_all(self, line):
        """List all instances or instances of a specific class."""
        arg_list = storage.all()
        args = line.split()

        if args:
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                new_instances = [str(obj) for key, obj in arg_list.items()
                                 if key.startswith(class_name + ".")]
                print(new_instances)
        else:
            all_instances = [str(obj) for obj in arg_list.values()]
            print(all_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
