# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param list1:
        :param list2:
        :return:

        Plan: merge 2nd into 1st
         1. traverse 1 and 2 from start
         2. compare current nodes at 1 and 2
         3. If 1.value < 2.value and 1.next.value <= 2.value
            then 1.current = 1.next
         3. If 1.value < 2.value and 1.next.value > 2.value
            then tempNode = 2
            tempNode.next = 1.next
            1.next = tempNode
            2.current = 2.next
        4. If at end of 1 and 2.current is not null
            append the remaining nodes of 2 to 1
        5. Return 1
        """

        tail = dummy = ListNode()
        # tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(9)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

asl = Solution()
list3 = asl.mergeTwoLists(list1, list2)

while list3:
    print(list3.val, end=', ')
    list3 = list3.next
