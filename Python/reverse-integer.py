# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        res = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return res if -2**31 <= res < 2 ** 31 else 0
