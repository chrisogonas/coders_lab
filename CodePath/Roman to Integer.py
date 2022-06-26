"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000 For example, 2 is written as II in Roman numeral, just two ones added
together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900. Given a roman numeral, convert it to an integer.

Examples:
    Example 1:
        Input: s = "III"
        Output: 3
        Explanation: III = 3.

    Example 2:
        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.

    Example 3:
        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Planning/Pseudocode:
1. Create a dictionary of Roman numbers keys and corresponding integer values
2. Traverse the input Roman string from right to left
3. If current Roman character has a value greater than the previous
    then add value to total
    else subtract the value from the total
4. return total

Special Cases:
    If input is empty or input length is zero, return None
"""

rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convert_roman_numeral_to_integer(roman):
    my_len = len(roman)
    my_int = rom_int[roman[my_len - 1]]

    if my_len == 1:
        return rom_int[roman]

    for i in range(my_len - 2, -1, -1):
        if rom_int[roman[i]] >= rom_int[roman[i + 1]]:
            my_int += rom_int[roman[i]]
        else:
            my_int -= rom_int[roman[i]]

    return my_int


# Testing
print(convert_roman_numeral_to_integer('I'))
print(convert_roman_numeral_to_integer('III'))
print(convert_roman_numeral_to_integer('LVIII'))
print(convert_roman_numeral_to_integer('MCMXCIV'))

# Evaluation
# Time efficiency - O(1)
# Space efficiency - O(1)
# Dictionary access is static time; Roman numerals are fixed size. However, if the Roman numeral length was limitless,
# then the time complexity would become O(n)
