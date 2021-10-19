"""
Given a matrix of integers matrix of size n*m, where each element matrix[i][j] represents the cost of
passing from that cell, create a function that returns the cost of the minimum cost path to go from the
top left cell to the bottom right cell, knowing that you can only move to the right or to the bottom.

Example 1:
Input: matrix = [[3, 12, 4, 7, 10], [6, 8, 15, 11, 4], [19, 5, 14, 32, 21], [1, 20, 2, 9, 7]]
Output: 54

Example 2:
Input: matrix = [[96, 72, 52, 54, 86, 58, 21, 19, 99], [71, 96, 1, 43, 44, 98, 40, 26, 24]]
Output: 496
"""


# Parameters:
#  matrix: List[List[int]]
# return type: int

# This recursion approach is 'greedy', and does not work all the time; works with matrix example 1, but not 2
def minimumCostPath_recursion(matrix, total=0, i=0, j=0):
    if j == i == 0:
        total = matrix[i][j]
    if i + 1 == len(matrix) and j + 1 == len(matrix[0]):
        return total
    if i < len(matrix) and j < len(matrix[0]):
        if i + 1 == len(matrix) and j < len(matrix[0]):  # last row, but not last column
            j += 1
        elif i + 1 < len(matrix) and j + 1 == len(matrix[0]):  # last column, but not last row
            i += 1
        elif i + 1 < len(matrix) and j + 1 < len(matrix[0]):  # neither last column, nor last row
            if matrix[i + 1][j] <= matrix[i][j + 1]:
                i += 1
            else:
                j += 1

        total += matrix[i][j]
        return minimumCostPath_recursion(matrix, total, i, j)


# This approach works all the time, with a more efficient time, but double space usage due to the 2nd matrix
# time complexity == space complexity == O(nm)
def minimumCostPath(matrix):
    lm = len(matrix)
    wm = len(matrix[0])

    # matrix 2 - costs
    costs = [[0] * wm for i in range(lm)]
    costs[0][0] = matrix[0][0]  # min value of cell zero is the same value

    # fill top row
    for i in range(1, wm):
        costs[0][i] = matrix[0][i] + costs[0][i - 1]

    # fill 1st column
    for i in range(1, lm):
        costs[i][0] = matrix[i][0] + costs[i - 1][0]

    # costs for rows > 0 and cols > 0
    for i in range(1, lm):
        for j in range(1, wm):
            costs[i][j] = matrix[i][j] + min(costs[i][j - 1], costs[i - 1][j])

    return costs[lm - 1][wm - 1]


matrix = [[3, 12, 4, 7, 10], [6, 8, 15, 11, 4], [19, 5, 14, 32, 21], [1, 20, 2, 9, 7]]
# matrix = [[96, 72, 52, 54, 86, 58, 21, 19, 99], [71, 96, 1, 43, 44, 98, 40, 26, 24]]
# tot = minimumCostPath_recursion(matrix)
tot = minimumCostPath(matrix)

print(tot)
