#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_tot = 0
    weight_tot = 0

    for score, weight in my_list:
        sum_tot += score * weight
        weight_tot += weight
    avg = sum_tot / weight_tot
    return avg
