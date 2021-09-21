"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].
"""


def product_of_all_except_one():
    arr = [1, 2, 3, 4, 5]
    arr2 = []

    # loop 1 - get total product of all
    product = 1  # default to 1
    for item in arr:
        product *= item

    # loop 2 - division and update array
    for i in range(len(arr)):
        arr2.insert(i, int(product / arr[i]))

    return arr2


print(product_of_all_except_one())
