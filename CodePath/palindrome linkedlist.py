#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(node):
    length = get_length(node)
    if length == 1:
        return True
    if length == 2:
        if node.val == node.next.val:
            return True
        else:
            return False

    first_half = []
    current_node = 0
    half = length // 2
    while current_node < half:
        first_half.append(node.val)
        node = node.next
        current_node += 1

    if length % 2 != 0:
        node = node.next

    while node:
        val = first_half.pop()
        if node.val != val:
            return False
        node = node.next

    return len(first_half) == 0 and node is None


def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length


# class Tests:
#     if __name__ == "__main__":
# 1
n1_1 = ListNode(val=1)
print(f"Test 1 - isPalindrome returned: {isPalindrome(n1_1)}, expected: True")

# 1 -> 2
n2_1 = ListNode(val=1)
n2_2 = ListNode(val=2)
n2_1.next = n2_2
print(f"Test 2 - isPalindrome returned: {isPalindrome(n2_1)}, expected: False")

# 1 -> 2 -> 3
n3_1 = ListNode(1)
n3_2 = ListNode(2)
n3_3 = ListNode(3)
n3_1.next = n3_2
n3_2.next = n3_3
print(f"Test 3 - isPalindrome returned: {isPalindrome(n3_1)}, expected: False")

# 1 -> 2 -> 1
n4_1 = ListNode(1)
n4_2 = ListNode(2)
n4_3 = ListNode(1)
n4_1.next = n4_2
n4_2.next = n4_3
print(f"Test 4 - isPalindrome returned: {isPalindrome(n4_1)}, expected: True")

# 1 -> 2 -> 1 -> 1
n4 = ListNode(1)
n4.next = ListNode(2)
n4.next.next = ListNode(2)
n4.next.next.next = ListNode(2)
n4.next.next.next.next = ListNode(1)

print(f"Test 4 - isPalindrome returned: {isPalindrome(n4)}, expected: True")
