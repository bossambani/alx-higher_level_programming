#!/usr/bin/python3
"""Defines a function module that converts
   the json string back to python object
"""
import json


def from_json_string(my_str):
    """
        Returns: The python object
    """
    return json.loads(my_str)
