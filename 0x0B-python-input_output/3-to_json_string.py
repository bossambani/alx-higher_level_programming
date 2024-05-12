#!/usr/bin/python3
"""Defines a function that converts python objects to JSON format"""
import json


def to_json_string(my_obj):
    """
        Args: The python object name
        Returns: JSON string
    """
    return json.dumps(my_obj)
