# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        num_dict = {}
        for i, v in enumerate(nums):
            num_dict.setdefault(v, [])
            num_dict[v].append(i + 1)
        for v in nums:
            vv = target - v
            if vv != v:
                if vv in num_dict:
                    return sorted([num_dict[v][0], num_dict[vv][0]])
            else:
                if len(num_dict[v]) > 1:
                    return sorted([num_dict[v][0], num_dict[v][1]])
