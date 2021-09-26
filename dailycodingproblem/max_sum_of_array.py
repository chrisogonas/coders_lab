"""
Take an array with positive and negative integers, and find the largest sum of the array elements,
not necessarily contiguous.
"""


def get_array_max_sum(arr):
    if len(arr) == 0:
        return print("Array is empty!")

    smallest_negative = 0
    max_sum = 0
    i = 0
    for item in arr:
        # get first negative number
        if item < 0 and i == 0:
            smallest_negative = item
            i += 1

        # get next smallest negative number and update accordingly
        elif item < 0 < i:
            if item > smallest_negative:
                smallest_negative = item

        # sum all positive numbers
        if item > 0:
            max_sum += item

    # get final maximum sum
    max_sum += smallest_negative

    return max_sum


max_add = get_array_max_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19])

print(max_add)
