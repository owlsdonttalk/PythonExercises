# https://leetcode.com/problems/add-two-numbers/
import functools
from typing import Optional
import timeit


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return

        result1 = []
        result2 = []

        self.read_linked_list(head=l1, result=result1)
        self.read_linked_list(head=l2, result=result2)

        num1 = 0
        for digit in result1[::-1]:
            num1 = num1 * 10 + digit

        num2 = 0
        for digit in result2[::-1]:
            num2 = num2 * 10 + digit

        newlist = [digit for digit in str(num1 + num2)]
        return self.list_to_linked_list(values=newlist)

    def read_linked_list(self, head: ListNode, result):
        if head is None:
            return
        else:
            result.append(head.val)
            if head.next is not None:
                self.read_linked_list(head.next, result)

    @staticmethod
    def list_to_linked_list(values):
        if not values:
            return None

        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            new_node = ListNode(val)
            current.next = new_node
            current = new_node

        return head


list3 = ListNode(3, None)
list2 = ListNode(4, list3)
list1 = ListNode(2, list2)

lost3 = ListNode(4, None)
lost2 = ListNode(6, lost3)
lost1 = ListNode(5, lost2)

s = Solution()

def my_method_wrapper():
    s.addTwoNumbers(l1=list1, l2=lost1)

elapsed_time = timeit.timeit(my_method_wrapper, number=1000)
print(f"Elapsed time: {elapsed_time:.6f} seconds")
