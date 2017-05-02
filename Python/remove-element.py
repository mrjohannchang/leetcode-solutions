# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        nums[:] = [n for n in nums if n != val]
        return len(nums)
