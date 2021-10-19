"""
Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit),
add them and return the resulting linked list. Here, the first node in a list represents the least significant digit.

Example:
    head1->1->0->9->9->NULL
    head2->7->3->2->NULL
    running head->8->3->1->0->1->NULL

NOTE: Please note that you do not need to implement the linkedlist and node classes in this case;
    just assume an input of 2 linked lists to the function sum_two_linked_lists
"""


def sum_two_linked_lists(list1, list2, carry_over=0):
    list3 = LinkedList()
    tempL = []
    while list1.head is not None or list2.head is not None:
        current1 = list1.head
        current2 = list2.head
        new_total = 0

        if current1 is not None and current2 is not None:
            new_total = current1.data + current2.data + carry_over
        elif current1 is None and current2 is not None:
            new_total = current2.data + carry_over
        elif current1 is not None and current2 is None:
            new_total = current1.data + carry_over

        tempL.append(new_total % 10)
        carry_over = new_total // 10

        if list1.head is not None:
            list1.head = current1.next

        if list2.head is not None:
            list2.head = current2.next

    if carry_over > 0:
        tempL.append(carry_over)

    [list3.insert(i) for i in tempL[::-1]]

    return list3


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

L3 = sum_two_linked_lists(L1, L2)
L3.printItems()
