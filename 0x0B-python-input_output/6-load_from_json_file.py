#!/usr/bin/python3
"""creates objects from a json file module"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        json_obj = json.load(f)
        return json_obj
