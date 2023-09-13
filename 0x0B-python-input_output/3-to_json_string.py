#!/usr/bin/python3
"""JSON representation of a string module"""

import json


def to_json_string(my_obj):
    """
    serializes a data to a string
    Args:
        my_obj: data to be serializes
    Returns:
        JSON representation of the object
    """
    json_string = json.dumps(my_obj)
    return json_string
