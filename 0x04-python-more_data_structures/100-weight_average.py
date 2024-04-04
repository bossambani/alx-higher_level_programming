#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    sum2 = 0
    if len(my_list) == 0:
        return 0
    for x in my_list:
        sum += prod(*x)
        sum2 += x[1]
    return sum/sum2


def prod(x, y):
    return x * y
