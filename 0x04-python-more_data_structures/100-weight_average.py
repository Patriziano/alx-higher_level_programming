#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for scores, weight in my_list:
        total_sum += scores * weight
        total_weight += weight

    if total_weight == 0
    return 0
    weighted_average = total_sum / total_weight
    return weighted_average
