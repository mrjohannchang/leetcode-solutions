# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        res = 0
        if not height:
            return res
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
            if l_max < r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1
        return res
