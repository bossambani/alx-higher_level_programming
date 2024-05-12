#!/usr/bin/python3
"""defines a function that adds all arguments to a python list,
   and then save them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_items.json", "a")
try:
    item = load_from_json_file("add_item.json")
except FileNotFoundError:
    item = []
item.extend(sys.argv[1:])
save_to_json_file(item, "add_item.json")
