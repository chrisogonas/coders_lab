"""
Given a string, return the reverse of the string:
e.g. given: 'The quick brown fox jumps over the lazy dog.'
return 'dog. lazy the over jumps fox brown quick The'
"""


def reverse_string(s):
    if s == '':
        return ''

    new_str = ''
    new_s = s.split(' ')
    arr_len = len(new_s) - 1

    for item in new_s[::-1]:
        new_str = f'{new_str} {item}'

    return new_str.strip()


my_str = reverse_string('The quick brown fox jumps over the lazy dog.')
print(my_str)
