class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient: int = 0

        if abs(dividend) < abs(divisor):
            return quotient

        remainder: int = 0
        i: int
        for i in range(len(str(abs(dividend)))):
            remainder = int(str(remainder) + '0') + int(str(abs(dividend))[i])
            quotient = int(str(quotient) + '0')

            if remainder < abs(divisor):
                continue

            j: int = 0
            k: int = abs(divisor)
            while k <= remainder:
                j += 1
                k += abs(divisor)

            quotient += j
            if abs(quotient) > 2**31:
                break
            remainder = remainder - k + abs(divisor)

        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            quotient = -quotient

        return min(quotient, 2**31 - 1) if quotient > 0 else max(quotient, -2**31)
