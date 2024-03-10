#!/usr/bin/python3
"""
Console module for the AirBnB clone project
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = "(hbnb) "
    
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def help_quit(self):
        """Print help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help for EOF command"""
        print("EOF command to exit the program")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    dedef do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        # objects = storage.all()

        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.CLASSES:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]

        # Store the previous updated_at value
        # prev_updated_at = obj.updated_at

        # Simplify attribute handling (without explicit checks)
        setattr(obj, attribute, value)

        storage.all()[key].save()

    # Help messages for each command
    def help_create(self):
        """Print help for create command"""
        print("Creates a new instance of BaseModel")

    def help_show(self):
        """Print help for show command"""
        print("Prints the string representation of an instance")

    def help_destroy(self):
        """Print help for destroy command"""
        print("Deletes an instance based on the class name and id")

    def help_all(self):
        """Print help for all command"""
        print("Prints all string representation of all instances")

    def help_update(self):
        """Print help for update command"""
        print("Updates an instance based on the class name and id")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

