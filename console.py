#!/usr/bin/python3
"""Define the HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage

def parse(text_args):
    """Parse all argurments for the console"""
    l_args = text_args.split(" ")
    return l_args[0:]

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
    ===========
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit with 'EOF' signal.
        """
        print("")
        return True

    def emptyline(self):
        """Ignore an empty line.
        """
        pass

    # Commands

    def do_create(self, arg):
        """Usage --> create <class>
        Create a new instance of the indicated class and:
            - Saves it (to the JSON file)
            - Prints the id

        Errors:
        =======
        ```
        (hbnb) create
        ** class name missing **
        ```

        ```
        (hbnb) create MyModel
        ** class doesn't exist **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        else:
            key_cls = l_args[0]
            obj = d_cls[key_cls]()
            print(obj.id)
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
