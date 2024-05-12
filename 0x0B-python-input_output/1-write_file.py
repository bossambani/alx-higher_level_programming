#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
