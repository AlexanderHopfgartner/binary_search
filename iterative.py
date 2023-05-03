from math import log2


def binary_search(searching_list: list[int], number: int):
    """Return the index of the number in the seaching_list.

    If the number is not included
    Return -1"""
    # Evaluate the current point.
    # Declares the last_high_point and las_low_point
    current_point = int(len(searching_list)/2)
    last_high_point = len(searching_list)
    last_low_point = 0
    # Declare the runtime check
    runtime = round(log2(len(searching_list))+0.5)
    # While the index(current_point) of the list is not the searching number AND the runtime counter is not over
    # Search for the right index(current_point)
    while searching_list[current_point] != number and runtime:
        # Reset the last_high_point with the current_point +1 if the number is still too low
        if number < searching_list[current_point]:
            last_high_point = current_point + 1
            current_point = (current_point - 1 + last_low_point) // 2
        # Reset the last_low_point with the current_point -1 if the number is still too high
        else:
            last_low_point = current_point - 1
            current_point = (current_point + 1 + last_high_point) // 2
        # -1 form the runtime per turn
        runtime -= 1
    # Return the index(current_point) if the item on the index of the list ist the same number
    if number == searching_list[current_point]:
        return current_point
    # Return -1 if the runtime is over cause of overflow thanks to math
    else:
        return -1
