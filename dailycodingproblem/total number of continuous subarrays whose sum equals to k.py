"""
 Question:
 Given an array of integers nums and integer k, return the total number of continuous sub-arrays whose sum equals to k.

 Input:
 nums=[1,1,1] k = 2
 output: 2
"""


def GetContSubArrays(arr, target_sum):
    current_sum = arr[0]  # default to the first array element
    count = 0
    left = right = 0

    while right < len(arr):
        if current_sum == target_sum:
            count += 1
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        elif current_sum > target_sum:
            current_sum -= arr[left]
            left += 1
        elif current_sum < target_sum:
            right += 1
            if right < len(arr):
                current_sum += arr[right]

    return count


print(GetContSubArrays([1, 2, 2, 2, 3, 3, 4], 4))
