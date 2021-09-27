"""
Given two sorted arrays, return an array of common elements of the two input arrays.
Example: Given [1, 3, 4, 5, 9] and [1, 4, 6, 8, 9], return [1, 4, 9]
"""


def common_elements_in_2_sorted_arrays(arr1, arr2):
    i = j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            yield arr1[i]
            i += 1
            j += 1

        if i >= len(arr1) and j >= len(arr2):
            break

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1


abc = common_elements_in_2_sorted_arrays([1, 3, 4, 5, 9], [1, 2, 4, 6, 7, 8, 9])
for item in abc:
    print(item, end=', ')