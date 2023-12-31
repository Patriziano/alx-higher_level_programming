#!/usr/bin/python3
"""Save to Json module"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object using json to a textfile

    Args
        my_obj: object file to be wriiten
        filename: name of file to write the object
        """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f, ensure_ascii=False)
