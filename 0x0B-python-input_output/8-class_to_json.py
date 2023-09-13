#!/usr/bin/python3
"""simple data structure for JSON serialization of object"""


def class_to_json(obj):
    """
    dictionary description of JSON serialization of  an object

    Args:
        obj(list,dict,str,int,bool): the simple data structure

    Returns:
        dict description for JSON serialization of an object
    """

    if isinstance(obj, dict):
        return obj

    # Get all the attributes of the object
    attributes = obj.__dict__

    serialized = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[key] = value

    return serialized
