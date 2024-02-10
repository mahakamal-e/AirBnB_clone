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

            if hasattr(instance, attr_name):
                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    print("** invalid value format **")
                    return

                setattr(instance, attr_name, attr_value)
                instance.updated_at = datetime.now()
                storage.save()
            else:
                print("** no attribute found **")
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
    '''
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
                    'count': self.do_count,
                    # Add more commands as needed
                }

                if command in command_dispatch:
                    return command_dispatch[command](
                        f"{class_name} {arguments[0]}")

                print("*** Unknown command: {}".format(command))

            else:
                print(f"** class doesn't exist **")

        except Exception as e:
            print("*** Unknown syntax: {}".format(line))
    '''
    
    def default(self, line):
        """Handle Cmd methods."""
        line_vector = line.split('.')
        class_argument = line_vector[0]

        if line_vector == []:
            print("*** Unknown syntax: {}".format(line))
            return

        try:
            line_vector = line_vector[1].split('(')
            command = line_vector[0]

            if command == 'all':  # <class name>.all
                HBNBCommand.do_all(self, class_argument)  # all BaseModel

            elif command == 'count':  # <class name>.count()
                HBNBCommand.do_count(self, class_argument)

            elif command == 'show':  # <class name>.show(<id>)
                line_vector = line_vector[1].split(')')
                id_argument = line_vector[0].strip("'\"")
                argument = class_argument + ' ' + id_argument
                HBNBCommand.do_show(self, argument)  # show BaseModel 123

            elif command == 'destroy':  # <class name>.destroy(<id>)
                line_vector = line_vector[1].split(')')
                id_argument = line_vector[0].strip("'\"")
                argument = class_argument + ' ' + id_argument
                HBNBCommand.do_destroy(self, argument)  # destroy BaseModel 122

            elif command == 'update':
                line_vector = line_vector[1].split(',')
                id_argument = line_vector[0].strip("'\"")
                name_argument = line_vector[1].strip(',')
                if "{" not in line:
                    value_argument = line_vector[2]
                    name_argument = name_argument.strip(" '\"")
                    value_argument = value_argument.strip(' )')
                if "{" in line:

                    b1 = line.index('{')
                    b2 = line.index('}')
                    value_dict = line[b1 + 1: b2].replace(" ", "")
                    value_dict_list = value_dict.split(",")

                    for s in value_dict_list:
                        s = s.split(":")
                        argument = class_argument + ' ' + id_argument + \
                            ' ' + s[0][1:-1] + ' ' + s[1]
                        HBNBCommand.do_update(self, argument)
                        key = class_argument + '.' + id_argument
                        if key not in storage.all().keys():
                            return
                else:
                    # If eval fails, use the attribute and value pattern
                    argument = class_argument + ' ' + id_argument + \
                        ' ' + name_argument + ' ' + value_argument
                    HBNBCommand.do_update(self, argument)

            else:
                print("*** Unknown syntax: {}".format(line))
                return

        except IndexError:
            print("*** Unknown syntax: {}".format(line))
    
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()