#!/usr/bin/python3
"""
Console module for the AirBnB clone project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
