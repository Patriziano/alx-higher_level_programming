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

    def to_json(self):
        """
        Retrieves a dictionary representation of a student instance
        """
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }
        return student_dict
