# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
