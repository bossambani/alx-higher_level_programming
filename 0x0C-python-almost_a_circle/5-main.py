#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    r3 = Rectangle(12, 10, 3, 6)
    print(r3)

    r3 = Rectangle(12, 10, 3, 6, 8)
    print(r3)



