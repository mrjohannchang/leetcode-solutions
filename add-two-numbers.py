# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        res = l3 = ListNode(0)
        notation = 0
        while True:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            l3.val = (l1_val + l2_val + notation) % 10
            notation = 1 if l1_val + l2_val + notation > 9 else 0
            if (l1 and l1.next) or (l2 and l2.next) or notation:
                l3.next = ListNode(0)
                l3 = l3.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            else:
                break
        return res
