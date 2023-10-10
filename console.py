#!/usr/bin/python3
import cmd
"""
Module  that contains the entry point of the python
command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

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
        """does nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
