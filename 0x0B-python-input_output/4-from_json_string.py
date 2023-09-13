#!/usr/bin/python3
"""Object(data structure) of a string module"""

import json


def from_json_string(my_str):
    """
   decodes a string to an object
    Args:
        my_str: string to be decodeded
    Returns:
        object of the string
    """
    json_obj = json.loads(my_str)
    return json_obj
