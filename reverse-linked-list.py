# -*- coding: utf-8 -*-


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev_head = None
        while head:
            curr_head = head
            head = head.next
            curr_head.next = prev_head
            prev_head = curr_head
        return prev_head
