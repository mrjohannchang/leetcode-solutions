import re


class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading whitespace
        s = re.sub('^\ +', '', s)

        if not s:
            return 0

        positive: bool = True

        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                positive = False
            s = s[1:]

        s = re.sub('^([0-9]*).*', r'\1', s)

        if not s:
            return 0

        n: int = int(s) * (1 if positive else -1)

        if n < -2**31:
            n = -2**31

        if n > 2**31 - 1:
            n = 2**31 - 1

        return n
