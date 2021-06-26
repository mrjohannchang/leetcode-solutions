class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        remainder: int = abs(numerator) % abs(denominator)

        if remainder == 0:
            return str(int(numerator / denominator))

        integer_quotient_str: str = \
            ("-" if (numerator >= 0 and denominator < 0 ) or (numerator < 0 and denominator > 0) else "") + \
            str(int(abs(numerator / denominator)))
        fractional_remainders: list[int] = [remainder]
        fractional_quotient_str: str = ""
        repeated: bool = False

        while remainder > 0:
            remainder *= 10

            if remainder >= abs(denominator):
                fractional_quotient_str += str(int(remainder / abs(denominator)))
                remainder %= abs(denominator)
                if remainder in fractional_remainders:
                    repeated = True
                    break
            else:
                fractional_quotient_str += "0"

            fractional_remainders.append(remainder)

        if repeated:
            fractional_quotient_str: str = \
                fractional_quotient_str[:fractional_remainders.index(remainder)] + "(" + \
                fractional_quotient_str[fractional_remainders.index(remainder):] + ")"

        return integer_quotient_str + "." + fractional_quotient_str
