from test import ordered_list
from math import log2


def binary_search(searching_list: list[int], number: int):
    current_point = int(len(searching_list)/2)
    last_highpoint = len(searching_list)
    last_low_point = 0
    runtime = round(log2(len(searching_list))+0.5)
    while searching_list[current_point] != number and runtime:
        if number < searching_list[current_point]:
            last_highpoint = current_point + 1
            current_point = (current_point - 1 + last_low_point) // 2
        else:
            last_low_point = current_point - 1
            current_point = (current_point + 1 + last_highpoint) // 2
        runtime -= 1
    if number == searching_list[current_point]:
        return current_point
    else:
        return -1


# print(ordered_list[binary_search(ordered_list, 97157)])
