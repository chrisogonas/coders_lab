"""
Take an array with positive and negative integers, and find the maximum continuous sum of the array.
"""


def max_array_contiguous_sum(arr):
    # base case
    if len(arr) == 0:
        return print("Array too small!")

    max_sum = current_sum = arr[0]

    for item in arr[1:]:
        current_sum = max(current_sum + item, item)
        max_sum = max(current_sum, max_sum)

    return max_sum


max_add = max_array_contiguous_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19])

print(max_add)