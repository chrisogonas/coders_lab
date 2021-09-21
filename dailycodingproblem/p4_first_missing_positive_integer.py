"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def first_missing_positive_integer():
    # arr = [3, 4, -1, 1, 2, 6, 5]
    arr = [-1, -3]
    my_store = {}

    # create a dict of vals above zero
    for i in arr:
        if i > 0:
            if i not in my_store:
                my_store[i] = i

    if len(my_store) == 0:
        return 1

    # get the first smallest missing positive integer
    for i in range(len(my_store)):
        temp: int = i + 1
        if temp not in my_store:
            return temp

    else:
        temp += 1
        return temp


num = first_missing_positive_integer()
print(f'Smallest missing +ve integer: {num}')
