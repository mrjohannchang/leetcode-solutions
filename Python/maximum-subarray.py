# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        res = section_sum = nums[0]
        if len(nums) == 1:
            return res
        for i in range(1, len(nums)):
            if section_sum < 0:
                section_sum = nums[i]
            else:
                section_sum += nums[i]
            res = max(res, section_sum)
        return res
