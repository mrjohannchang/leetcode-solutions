# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        l = 0
        d = {}
        res = len(d)
        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1
            d[s[r]] = r
            res = max(res, r - l + 1)
        return res
