# -*- coding: utf-8 -*-

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(w for w in reversed(s.split(' ')) if w)
