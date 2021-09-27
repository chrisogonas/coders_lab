"""
Given an integer (positive or negative), create a recursive function that returns the sum of its digits
Example 1: input: n = 425
    output: 11
Example 2: input: n = 8009
    output: 17
"""


def sum_of_digits(n, dsum=0):
    if n < 0:
        return sum_of_digits(-n)
    elif n < 10:
        return n + dsum
    else:
        return sum_of_digits(n // 10, dsum + n % 10)


print(sum_of_digits(425))
