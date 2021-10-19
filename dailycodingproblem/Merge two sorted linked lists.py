"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

Consider two sorted linked lists as an example.
    head1->4->8->15->19->NULL
    head2->7->9->10->16->NULL

The merged linked list should look like this:
    head1->4->7->8->9->10->15->16->19->NULL

NOTE: This solution is incomplete, and it has bugs
    TODO: Fix the bugs
"""


def merge_sorted_linked_lists(list1, list2):
    return_head = None
    lead_head = None
    head2 = None

    if list1.head.data <= list2.head.data:
        return_head = lead_head = list1.head
        head2 = list2
    else:
        return_head = lead_head = list2.head
        head2 = list1.head

    while lead_head.next is not None and head2.next is not None:

        if lead_head.next.data <= head2.data:
            lead_head = lead_head.next
        elif lead_head.next.data > head2.data:
            temp = lead_head.next
            lead_head = head2
            head2 = temp

    return return_head


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printItems(self):
        current = self.head
        while current.next:
            print(current.data, end=' ')
            current = current.next

        print(current.data)  # print last item


# Singly Linked List with insertion and print methods
L1 = LinkedList()
L2 = LinkedList()

L1.insert(4)
L1.insert(4)
L1.insert(5)
L1.printItems()

# L1.insert(9)
# L1.insert(9)
# L1.insert(0)
# L1.insert(1)
# L1.printItems()

L2.insert(8)
L2.insert(5)
L2.insert(6)
L2.insert(2)
L2.printItems()

# L2.insert(2)
# L2.insert(3)
# L2.insert(7)
# L2.printItems()

L3 = merge_sorted_linked_lists(L1, L2)
L3.printItems()
