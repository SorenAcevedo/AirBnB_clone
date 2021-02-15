#!/usr/bin/python3
"""Define the HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split

def parse(text_args):
    """Parse all argurments for the console"""
    return split(text_args)

def cast(text_value):
    """Cast in int or float a value"""

    if text_value.isnumeric():
        return int(text_value)
    else:
        try:
            return float(text_value)
        except:
            return text_value


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

    def do_show(self, arg):
        """Usage --> show <class> <id>
        Prints the string representation of an instance
        based on the class name and id

        Errors:
        =======
        ```
        (hbnb) show
        ** class name missing **
        ```

        ```
        (hbnb) show MyModel 1234-1234
        ** class doesn't exist **
        ```

        ```
        (hbnb) show BaseModel
        ** instance id missing **
        ```

        ```
        (hbnb) show BaseModel 12341234
        ** no instance found **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key_obj])

    def do_destroy(self, arg):
        """Usage --> destroy <class> <id>
        Deletes an instance based on the class name and id,
        also update the JSON file.

        Errors:
        =======
        ```
        (hbnb) destroy
        ** class name missing **
        ```

        ```
        (hbnb) destroy MyModel 1234-1234
        ** class doesn't exist **
        ```

        ```
        (hbnb) destroy BaseModel
        ** instance id missing **
        ```

        ```
        (hbnb) destroy BaseModel 12341234
        ** no instance found **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key_obj]
                storage.save()

    def do_all(self, arg):
        """Usage --> all <class>
        Prints all string representation of all instances
        based or not on the class name.
        Note: <class> is optional.

        Errors:
        =======
        ```
        (hbnb) all MyModel
        ** class doesn't exist **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes
        val_obj = storage.all().values()

        if len(l_args) == 0:
            print([str(obj) for obj in val_obj])
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in val_obj if obj.__class__.__name__ == l_args[0]])

    def do_update(self, arg):
        """Usage --> update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding or updating attribute
        also update the JSON file.

        Errors:
        =======
        ```
        (hbnb) update
        ** class name missing **
        ```

        ```
        (hbnb) update MyModel 1234-1234
        ** class doesn't exist **
        ```

        ```
        (hbnb) update BaseModel
        ** instance id missing **
        ```

        ```
        (hbnb) update BaseModel 12341234
        ** no instance found **
        ```

        ```
        (hbnb) update BaseModel existing-id
        ** attribute name missing **
        ```

        ```
        (hbnb) update BaseModel existing-id first_name
        ** value missing **
        ```
        """

        l_args = parse(arg)
        d_cls = HBNBCommand.__classes

        if len(l_args) == 0:
            print("** class name missing **")
        elif l_args[0] not in d_cls.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            key_obj = l_args[0] + "." + l_args[1]
            if key_obj not in storage.all().keys():
                print("** no instance found **")
            elif len(l_args) == 2:
                print("** attribute name missing **")
            elif len(l_args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key_obj]
                attr = l_args[2]
                value = cast(l_args[3])
                setattr(obj, attr, value)
                storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
