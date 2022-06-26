"""
Longest Consecutive Subsequence

Given an unsorted array of integers, find the length of the longest subsequence such that elements in the
subsequence are consecutive integers. The consecutive numbers can be in any order.

Examples:
    Input: [1, 9, 3, 10, 4, 20 , 2]
    Output: 4
    [1, 3, 4, 2] is the longest subsequence of consecutive elements.

APPROACH/PLAN
0. create a set
1. add all elements into the set
2. in a 2nd loop, for each element, check if element-1 or element+1 exists in set
    if above condition is met, retain, else remove
3. return the set items

# Test Case
- 1 set of consecutive sequence
- Multiple set of consecutive sequences
"""


# Implementation
def get_lcs(arr):
    eset = set()
    eset.update(arr)

    for i in eset:
        if i-1 not in eset and i+1 not in eset:
            arr.remove(i)


    # Now extract LCS from arr; arr contains all subsequences
    # TODO - code here

    return arr


arr_in = [1, 9, 3, 10, 4, 20, 2]
print(get_lcs(arr_in))
