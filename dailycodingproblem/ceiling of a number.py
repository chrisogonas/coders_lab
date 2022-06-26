"""
Return ceiling of a number from a given array.
    - Find smallest number equal to or greater than the target number
"""


def get_ceiling(arr, left, right, number):
    if right >= left:

        # special cases
        # item is less than smallest array item
        if number <= arr[left]:
            return arr[left]

        # item is larger than largest array item
        if number > arr[right]:
            return -1

        mid = left + (right - left) // 2

        # number == mid, return mid value
        if arr[mid] == number:
            return arr[mid]
        elif arr[mid] < number:
            if left < right and number <= arr[mid + 1]:
                return arr[mid + 1]
            elif left < right and number > arr[mid + 1]:
                return get_ceiling(arr, mid + 1, right, number)
            elif left == right:
                return -1
            # return get_ceiling(arr, mid + 1, right, number)
        elif arr[mid] > number:  # and number < arr[mid - 1]:
            if left < right and number <= arr[mid - 1]:
                return get_ceiling(arr, left, mid - 1, number)
            elif left < right and number > arr[mid - 1]:
                return get_ceiling(arr, mid + 1, right, number)
            elif left == right:
                return -1

    else:
        return -1  # not found


arr = [2, 4, 5, 6, 8, 9, 11, 15]
target = 12
result = get_ceiling(arr, 0, len(arr) - 1, target)

if result == -1:
    print('Item not found')
else:
    print(f'Item {result} found.')
