"""
Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in
the array. The array has to be modified in-place.
"""


def move_zeros_left(arr):
    if len(arr) == 0:
        return None

    current0 = -1
    l = len(arr) - 1
    for i, item in enumerate(arr[::-1]):
        if i == 0:
            if item == 0:
                current0 = l
            continue

        if item > 0:
            arr[current0] = item
            arr[l - i] = 0
            current0 -= 1
        if item == 0:
            if current0 == -1:
                current0 = l - i  # where array last number is greater than zero and 1st zero occurs after.
            continue

    return arr


a = move_zeros_left([0, 1, 10, 20, 0, 59, 63, 0, 88, 0, 0, 99])

print(a)
