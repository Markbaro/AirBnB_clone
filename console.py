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

    def do_show(self, line):
        """Show details of a specific instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        allobjects = storage.all()
        key = f"{args[0]}.{args[1]}"
        found = allobjects.get(key, None)

        if found:
            print(found)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance using class name and instance ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            allobjects = storage.all()

            if key in allobjects:
                del allobjects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        class_name = args[0]
        count = sum(1 for key in storage.all()
                    if key.startswith(class_name + "."))
        print(count)

    def do_update(self, arg):
        """
        Update an instance based on class name,
        ID, attribute name, and value.
        """
        args = arg.split()

        if not args:
            print('** class name missing **')
            return
        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]

        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()

        if key in all_objects:
            instance = all_objects[key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
