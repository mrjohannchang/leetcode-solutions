# -*- coding: utf-8 -*-

# O(N^2)
# class Solution:
    # # @param {string} s
    # # @return {string}
    # def longestPalindrome(self, s):
        # length = 0
        # r = 0
        # m = [[0] * len(s) for _ in range(len(s))]
        # d = {}
        # for i in range(len(s)):
            # if s[i] not in d:
                # d[s[i]] = []
            # d[s[i]].append(i)
        # for i, v in enumerate(reversed(s)):
            # for j in d[v]:
                # m[i][j] = 1
                # if i > 0 and j > 0:
                    # m[i][j] += m[i-1][j-1]
                # if m[i][j] > length:
                    # length = m[i][j]
                    # r = i
        # return s[r-length+1:r+1]

# # O(N)
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        def match_len(t, i, j=None):
            if j is None:
                j = i
            k = 0
            while t[i] == t[j]:
                k += 1
                i -= 1
                j += 1
            return k

        t = '^.' + '.'.join(list(s)) + '.$'
        z = [0] * len(t)
        l = r = 0
        anchor = length = 0

        for i in range(1, len(t) - 1):
            if i > r:
                z[i] = match_len(t, i)
                l = i - z[i] + 1
                r = i + z[i] - 1
            else:
                ii = l + r - i
                j = ii - z[ii] + 1
                if j > l:
                    z[i] = z[ii]
                elif j == l:
                    z[i] = z[ii] + match_len(t, i - z[ii], i + z[ii])
                else:
                    z[i] = r - i + 1
            if z[i] > length:
                length = z[i]
                anchor = i

        res = ''
        for i in range(length):
            if t[anchor+i] == '.':
                continue
            if i == 0:
                res = t[anchor]
            else:
                res = t[anchor-i] + res + t[anchor+i]

        return res
