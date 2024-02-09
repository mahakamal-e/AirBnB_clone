#!/usr/bin/env python3
""" This module contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
import os
import sys

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Print Python path
print("Python Path:", sys.path)

from models import storage
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review



class HBNBCommand(cmd.Cmd):
    """ Implementation of class HBNBCommand """
    prompt = "(hbnb) "

    classes_names = {"BaseModel": BaseModel}
    # "State": State, "State": State,
    #                 "City": City, "Amenity": Amenity,
    #                 "Place": Place, "Review": Review, "User": User}
    
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
        Method thst printsthe string representation of an instance,
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
        """ Method that prints all string representation,
        of all instances based or not on the class name """
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
            attribute_name = input_args[2]
            attribute_value = input_args[3]
            setattr(instance, attribute_name, attribute_value)
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
