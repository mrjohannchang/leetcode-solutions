# -*- coding: utf-8 -*-

import bisect


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) < 2 or k == 0:
            return False
        w = [nums[0]]
        for i, v in enumerate(nums[1:]):
            j = bisect.bisect_left(w, v)
            if j < len(w):
                if abs(w[j] - v) <= t:
                    return True
            if j > 0:
                if abs(w[j-1] - v) <= t:
                    return True
            w.insert(j, v)
            if len(w) > k:
                w.pop(bisect.bisect_left(w, nums[i+1-k]))
        return False
