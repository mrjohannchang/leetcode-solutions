# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        p = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                res.append(str(nums[i]) if p == i else (str(nums[p]) + '->' + str(nums[i])))
                p = i + 1
        return res
