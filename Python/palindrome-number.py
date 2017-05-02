# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        y = x
        z = 0
        while y > 0:
            z = z * 10 + y % 10
            y /= 10
        return z == x
