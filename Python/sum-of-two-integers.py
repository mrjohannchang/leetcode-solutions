#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def add(self, a, b):
        bin_a, bin_b = str(bin(a))[2:], str(bin(b))[2:]
        length = max(len(bin_a), len(bin_b))
        bin_a, bin_b = bin_a.zfill(length), bin_b.zfill(length)
        res = []
        carry = '0'
        for i, j in zip(bin_a[::-1], bin_b[::-1]):
            operands = [i, j, carry]
            if operands.count('1') == 3:
                carry = '1'
                res.insert(0, '1')
            elif operands.count('1') == 2:
                carry = '1'
                res.insert(0, '0')
            elif operands.count('1') == 1:
                carry = '0'
                res.insert(0, '1')
            elif operands.count('1') == 0:
                carry = '0'
                res.insert(0, '0')
            else:
                raise ValueError('operands: ' + ' '.join(operands))
        if carry == '1':
            res.insert(0, '1')
            carry = 0
        return int(''.join(res), 2)
    def substract(self, a, b):
        bin_a, bin_b = str(bin(a))[2:], str(bin(b))[2:]
        length = max(len(bin_a), len(bin_b))
        bin_a, bin_b = list(bin_a.zfill(length)), list(bin_b.zfill(length))
        has_debt = False
        res = []
        for i in range(length - 1, -1, -1):
            if has_debt:
                if bin_a[i] == '1' and bin_b[i] == '1':
                    res.insert(0, '1')
                elif bin_a[i] == '1' and bin_b[i] == '0':
                    res.insert(0, '0')
                    has_debt = False
                elif bin_a[i] == '0' and bin_b[i] == '1':
                    res.insert(0, '0')
                elif bin_a[i] == '0' and bin_b[i] == '0':
                    res.insert(0, '1')
            else:
                if bin_a[i] == '1' and bin_b[i] == '1':
                    res.insert(0, '0')
                elif bin_a[i] == '1' and bin_b[i] == '0':
                    res.insert(0, '1')
                elif bin_a[i] == '0' and bin_b[i] == '1':
                    res.insert(0, '1')
                    has_debt = True
                elif bin_a[i] == '0' and bin_b[i] == '0':
                    res.insert(0, '0')
        return int(''.join(res), 2)
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0
        if a >= 0 and b >= 0:
            res = self.add(a, b)
        elif a < 0 and b < 0:
            res = -self.add(-a, -b)
        elif a >= 0 and b < 0:
            if a >= abs(b):
                res = self.substract(a, -b)
            else:
                res = -self.substract(-b, a)
        elif a < 0 and b >= 0:
            if b >= abs(a):
                res = self.substract(b, -a)
            else:
                res = -self.substract(-a, b)
        return res
