from test import ordered_list
from math import log2


def binary_search(searching_list: list[int], number: int, *args):
    if args:
        mid = (args[0] + args[1]) // 2
        print(mid, args)
        if searching_list[mid] < number:
            number = binary_search(searching_list, number, mid + 1, args[1])
        elif searching_list[mid] > number:
            number = binary_search(searching_list, number, args[0], mid + 1)
        elif args[0] == args[1]:
            number = -1
    else:
        number = binary_search(searching_list, number, 0, len(searching_list)-1)
    return number


print(binary_search([x for x in range(0, 101)], 100))
