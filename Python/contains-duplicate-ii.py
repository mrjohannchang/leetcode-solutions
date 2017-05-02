# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, p in enumerate(nums):
            if p in d:
                d[p].append(i)
            else:
                d[p] = [i]
        for key in d:
            if len(d[key]) > 1:
                for i, p in enumerate(d[key][:-1]):
                    for j, q in enumerate(d[key][i+1:]):
                        if abs(p - q) <= k:
                            return True
        return False
