"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def message_decode_count(m):
    if m=='':
        return 1
    if m[0] == '0':
        return 0
    else:
        if len(m[1:]) == 2:
            if int(m[1:]) > 26:
                return 0
            else:
                return 1
        elif len(m[1:]) > 2:
            return 1 + message_decode_count(m[1:])