#!/usr/bin/python3
def best_score(a_dictionary):
    H_score = -100
    name = None
    if a_dictionary == name or len(a_dictionary) == 0:
        return None
    for k, v in a_dictionary.items():
        if v > H_score:
            H_score = v
            name = k
    return name
