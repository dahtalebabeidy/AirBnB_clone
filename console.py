```python
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
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attribute_name = args[2]
                attribute_value = args[3]
                # Handling quoted strings
                if attribute_value[0] == '"' and attribute_value[-1] == '"':
                    attribute_value = attribute_value[1:-1]
                try:
                    attribute_value = eval(attribute_value)
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                except Exception:
                    print("** value missing **")

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
```
