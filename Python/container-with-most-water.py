# -*- coding: utf-8 -*-


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        l = r = None
        res = 0
        for h, i in reversed(sorted([h, i] for i, h in enumerate(height))):
            if l is None:
                l = i
            if r is None:
                r = i
            if i < l:
                l = i
            if i > r:
                r = i
            res = max(res, min(height[l], height[r]) * (r - l))
        return res

print(Solution().maxArea([2,1]))
