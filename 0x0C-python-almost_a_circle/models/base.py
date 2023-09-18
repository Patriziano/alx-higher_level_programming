#!/usr/bin/python3
"""Base class module"""
import json
import os


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor that imitializeds the id attribute

        Args:
        id (int): The id of the Base class

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Dictionary to JSON string reprensation

        Args:
            list_dictionaries
        Returns:
            String representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        function that returns the list of the JSON string rep json_string

        Args:
            json_string: string representing a list of dictionaries

        Returns:
            returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base

        Returns:
            JSON string representation of obj_list written to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set based
        on the provided dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                if json_data:
                    dict_list = cls.from_json_string(json_data)
                    instances = [cls.create(**d) for d in dict_list]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
