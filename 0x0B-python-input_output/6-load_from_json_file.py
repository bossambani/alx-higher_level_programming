#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
        Args: filename is the name of the file
    """
    with open(filename, mode="r") as file:
        return json.load(file)
