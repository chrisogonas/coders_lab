"""
Given an integer N, return the longest binary gap surrounded by 1s
Examples:
    N=1041 returns 5 i.e. binary of 1041 = 10000010001 hence the longest contiguous zeros gap is 5
    N=9, binary = 1001, returns 2
    N=32, binary = 100000, returns zero since the gap is not enclosed by 1s
"""


def solution(N):
    # write your code in Python 3.6

    # Approach - sliding window

    # get binary of N
    n_bin = [int(x) for x in list('{0:0b}'.format(N))]

    left = 0
    counter = 0
    gap = 0
    for index, value in enumerate(n_bin):
        if index == 0 and value == 1:
            left = 0
        elif index > 0 and value == 1:
            left = index
            if counter > gap:
                gap = counter
                counter = 0 # reset counter
        else:
            counter += 1

    return gap


n = solution(3230)
print(n)