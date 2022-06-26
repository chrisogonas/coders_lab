"""
Reverse a linked list
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverse_llist(head):
    """
    :param head:
    :return: head of reversed list

    Pseudocode:
    NOTE: if list is null or empty, return None; if single node, return same list
    1. use variables current to hold current node, and previous to hold last node whose pointer was reversed
    2. traverse list from head to last node
    """

    if head is None:
        return None

    if head.next is None:
        return head

    current = head
    previous = None
    while current:
        temp = current
        current = current.next
        temp.next = previous
        previous = temp

    return previous


def print_list(list_head):
    while list_head:
        print(list_head.data, end='->')
        list_head = list_head.next

    print('None')


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print_list(head)
rev_head = reverse_llist(head)
print_list(rev_head)

