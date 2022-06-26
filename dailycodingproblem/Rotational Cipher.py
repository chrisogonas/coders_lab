"""
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""


# Add any extra import statements you may need here


# Add any helper functions you may need here

def create_alpha_dict():
    new_dict = {}
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for i in alpha:
        new_dict[i] = i

    return new_dict


def create_nums_dict():
    new_dict = {}
    for i in range(10):
        new_dict[str(i)] = str(i)

    return new_dict


def rotationalCipher(input, rotation_factor):
    # Write your code here
    alpha = create_alpha_dict()
    nums = create_nums_dict()

    output = []
    input_lower = input.lower()
    for index, i in enumerate(list(input_lower)):
        if i in alpha:
            index_i = list(alpha.keys()).index(i)
            new_index = index_i + rotation_factor

            if new_index > (len(alpha) - 1):
                new_index = new_index % len(alpha)

            new_key = list(alpha.keys())[new_index]
            new_value = alpha[new_key]
            if input[index].isupper():
                new_value = new_value.upper()
            output.append(new_value)

        elif i in nums:
            index_i = list(nums.keys()).index(i)
            new_index = index_i + rotation_factor

            if new_index > (len(nums) - 1):
                new_index = new_index % len(nums)

            new_key = list(nums.keys())[new_index]
            new_value = nums[new_key]

            output.append(new_value)

        else:
            output.append(i)

    return ''.join(output)


inp = 'abcdZXYzxy-999.@'
# inp = 'abcdzxyzxy-999.@'
rotation = 200
abc = rotationalCipher(inp, rotation)
print(f'Original: {inp}')
print(f'Rotation:', rotation)
print(f'Output: {abc}')

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

# def printString(string):
#     print('[\"', string, '\"]', sep='', end='')
#
#
# test_case_number = 1
#
#
# def check(expected, output):
#     global test_case_number
#     result = False
#     if expected == output:
#         result = True
#     rightTick = '\u2713'
#     wrongTick = '\u2717'
#     if result:
#         print(rightTick, 'Test #', test_case_number, sep='')
#     else:
#         print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
#         printString(expected)
#         print(' Your output: ', end='')
#         printString(output)
#         print()
#     test_case_number += 1
#
#
# if __name__ == "__main__":
#     input_1 = "All-convoYs-9-be:Alert1."
#     rotation_factor_1 = 4
#     expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
#     output_1 = rotationalCipher(input_1, rotation_factor_1)
#     check(expected_1, output_1)
#
#     input_2 = "abcdZXYzxy-999.@"
#     rotation_factor_2 = 200
#     expected_2 = "stuvRPQrpq-999.@"
#     output_2 = rotationalCipher(input_2, rotation_factor_2)
#     check(expected_2, output_2)
#
#     # Add your own test cases here
