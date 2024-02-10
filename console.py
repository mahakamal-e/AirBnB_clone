#!/usr/bin/env python3
""" This module contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ Implementation of class HBNBCommand """
    prompt = "(hbnb) "

    classes_names = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """ Do nothing on Empty line """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel """
        if not line:
            print("** class name missing **")
            return
        else:
            try:
                class_name = eval(line)()
                class_name.save()
                print(class_name.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Method that prints the string representation of an instance,
        based on the class name and id
        """
        input_args = line.split()

        if len(input_args) == 0:
            print("** class name missing **")
            return

        elif len(input_args) == 1:
            print("** instance id missing **")
            return
        elif input_args[0] not in self.classes_names:
            print("** class doesn't exist **")
            return
        elif len(input_args) != 2:
            print("** instance id missing **")
            return
        class_name = input_args[0]
        instance_id = input_args[1]

        if class_name not in self.classes_names:
            print("** class doesn't exist **")
            return

        objs_class = storage.all()
        key = f"{class_name}.{instance_id}"

        if key in objs_class:
            print(objs_class[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Method that Deletes an instance based on the class name and id

        Args:
            line: input command.
        """
        input_args = line.split()
        if len(input_args) == 0:
            print("** class name missing **")
            return

        elif input_args[0] not in self.classes_names:
            print("** class doesn't exist **")
            return

        elif len(input_args) != 2:
            print("** instance id missing **")
            return
        objs_class = storage.all()
        key = input_args[0] + "." + input_args[1]
        if key in objs_class.keys():
            del objs_class[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Method that prints all string representation,
        of all instances based or not on the class name
        """
        input_args = line.split()
        class_name = input_args[0] if input_args else None
        if class_name not in self.classes_names:
            print("** class doesn't exist **")
            return
        objs_class = storage.all()
        list_of_str = [str(value) for key, value in objs_class.items()
                       if not class_name or key.startswith(class_name)]
        print(list_of_str)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        input_args = line.split()
        if not input_args:
            print("** class name missing **")
            return
        elif input_args[0] not in self.classes_names:
            print("** class doesn't exist **")
            return
        elif len(input_args) < 2:
            print("** instance id missing **")
            return
        elif len(input_args) < 3:
            print("** attribute name missing **")
            return
        elif len(input_args) < 4:
            print("** value missing **")
            return
        key = input_args[0] + "." + input_args[1]
        objs_class = storage.all()
        if key in objs_class:
            instance = objs_class[key]
            attr_name = input_args[2]
            attr_value = input_args[3]
            setattr(instance, attr_name, attr_value)
            storage.save()
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """ quit from the program """
        return True

    def do_EOF(self, line):
        """ Exit from the program when End Of File """
        return True

    def help_quit(self):
        """ Help Message for Quit from the program """
        print("Quit command to exit the program")

    def do_count(self, line):
        """
        Method that counts the number of instances of a class

        Usage: <class name>.count().
        """
        input_args = line.split()
        class_name = input_args[0] if input_args else None
        if class_name not in self.classes_names:
            print("** class doesn't exist **")
            return
        count = 0
        instance_dict = storage.all()
        for key in instance_dict.keys():
            if key.startswith(class_name + "."):
                count += 1
        print(count)

    def default(self, line):
        """
        handle unknown or unsupported commands by parsing the input,
        and attempting to call specific methods based on the structure,
        of the command.
        """
        try:
            split_input = line.split('.')
            class_name = split_input[0]
            command_name = split_input[1]

            if '(' in command_name:
                split_res = command_name.split('(', 1)
                command = split_res[0]
                if len(split_res) > 1:
                    arguments_str = split_res[1].rstrip(')').strip()
                else:
                    arguments_str = ""

                arguments = []
                if ',' in arguments_str:
                    args_list = arguments_str.split(',')
                    for arg in args_list:
                        stripped_arg = arg.strip()
                        arguments.append(stripped_arg)
                else:
                    arguments = [arguments_str]

            else:
                command = command_name
                arguments = []

            if class_name in self.classes_names:
                cls = self.classes_names[class_name]

                command_dispatch = {
                    'all': self.do_all,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update,
                    'count': self.do_count
                }

                if command in command_dispatch:
                    return command_dispatch[command](
                        f"{class_name} {arguments[0]}")

                print("*** Unknown command: {}".format(command))

            else:
                print(f"** class doesn't exist **")

        except Exception as e:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
