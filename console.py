#!/usr/bin/python3
"""
Console module for the AirBnB clone project
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = "(hbnb) "

    # Existing commands (quit, EOF, emptyline, help_quit, help_EOF) remain unchanged.

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    storage.all().pop(key)
                    storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        instances = storage.all().values()
        if not arg:
            print([str(instance) for instance in instances])
        else:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                filtered_instances = [str(instance) for instance in instances
                                     if instance.__class__.__name__ == args[0]]
                print(filtered_instances)

    def do_update(self, arg):
        """Updates an instance attribute value"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = storage.all()[args[0] + "." + args[1]]
            setattr(instance, args[2], args[3])
            instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
