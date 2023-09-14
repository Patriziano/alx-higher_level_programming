#/usr/bin/python3
"""JSON rep object addition module"""
from sys import argv
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_arguments_to_list(arguments):
    if os.path.exists("add_item.json"):
        existing_list = load_from_json_file("add_item.json")
    else:
        existing_list = []
    existing_list.extend(arguments)
    return existing_list

if __name__ == "__main__":
# Get command-line arguments (excluding the script name)
    arguments = argv[1:]
    if arguments:
        updated_list = add_arguments_to_list(arguments)
        save_to_json_file(updated_list, "add_item.json")
#       print("Arguments added to 'add_item.json'.")
#   else:
#        print("No arguments provided.")
