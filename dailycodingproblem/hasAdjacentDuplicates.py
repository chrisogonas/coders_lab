"""
Given a string s, create a recursive boolean function that checks if it has
adjacent duplicates (the same character appearing in two successive indexes)

Example s:
input: str = "programming"
output: true
"""


# Parameters:
#  s: str
# return type: bool

def hasAdjacentDuplicates(s):
    if len(s) < 2:
        return False
    else:
        return True if s[0] == s[1] else hasAdjacentDuplicates(s[1:])


aa = hasAdjacentDuplicates('pprogramming')
print(aa)
