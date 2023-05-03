def binary_search(searching_list: list[int], number: int, *args):
    """Return the index of the number in the seaching_list.

    If the number is not included
    Return -1"""
    # Checks if it is the first time run else args will be set
    if args:
        mid = (args[0] + args[1]) // 2
        # As long the low point ist smaller or equal to the high point it will search
        if args[0] <= args[1]:
            # Return the index(mid) if the number is on the current location
            if searching_list[mid] == number:
                return mid
            # Checks if the index(mid) is still too low and recall self with the new mid +1 as new low
            if searching_list[mid] < number:
                number = binary_search(searching_list, number, mid + 1, args[1])
            # Checks if the index(mid) is still too high and recall self with the new mid -1 as new high
            elif searching_list[mid] > number:
                number = binary_search(searching_list, number, args[0], mid - 1)
        # Return -1 if the low is too high or the high is too low compared to the other
        # Cause the value is not in the list
        else:
            number = -1
    # Recall with the expected start *args
    else:
        number = binary_search(searching_list, number, 0, len(searching_list)-1)
    # Final return
    return number
