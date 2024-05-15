#!/usr/bin/python3
"""Defines a function module that writes an object
   to a text file, using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Args: my_obj is the object name to be saved in the file
              filename is the name of the file where the object is to be saved

    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
