#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integer = set(my_list)
    if not unique_integer:
        return 0
    integer_list = list(unique_integer)
    result = 0
    for element in integer_list:
        result += element
    return result
