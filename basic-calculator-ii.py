# -*- coding: utf-8 -*-

import re


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        res = 0
        add_sub_expression = iter(['+'] + re.split('([+-])', s))
        for add_sub_operator in add_sub_expression:
            mul_div_expression = iter(['*'] + re.split('([*/])', next(add_sub_expression)))
            mul_div_val = 1
            for mul_div_operator in mul_div_expression:
                if mul_div_operator == '*':
                    mul_div_val *= int(next(mul_div_expression))
                else:
                    mul_div_val /= int(next(mul_div_expression))
            if add_sub_operator == '+':
                res += mul_div_val
            else:
                res -= mul_div_val
        return res
