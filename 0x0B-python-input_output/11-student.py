#!/usr/bin/python3
"""The class module"""


class Student:
    """The class that defines the student"""
    def __init__(self, first_name, last_name, age):
        """
        The initialization with the constructor
        Args:
            first_name(str): Student's first name
            last_name(str): Student's last name
            age(int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student instance
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict

    def reload_from_json(self, json):
        """
        A function that replaces all attributes of the Student instance

        Args:
        json: The data structure
        """
        for key, values in json.items():
            setattr(self, key, values)
