# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        n = len(s)
        res = ''
        for i in range(numRows):
            if i >= n:
                break
            if i == 0 or i == numRows - 1:
                res += s[i::(numRows-1)*2 if (numRows-1)*2 > 0 else 1]
            else:
                k = i
                down = True
                while k < n:
                    res += s[k]
                    if down:
                        k += (numRows - 1 - i) * 2
                    else:
                        k += (i - 0) * 2
                    down = not down
        return res
