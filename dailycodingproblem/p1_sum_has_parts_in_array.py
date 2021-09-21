"""
Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.
"""

def array_has_numbers():
    my_list = [10, 15, 3, 7, 4]
    k = 19
    my_dict = {}

    for item in my_list:
        temp = k - item
        if temp in my_dict:
            return True
        else:
            my_dict.update({item: item})

    return False


abc = array_has_numbers()

print(abc)
