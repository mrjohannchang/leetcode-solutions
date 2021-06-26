class Solution:
    def intToRoman(self, num: int) -> str:
        symbol: str = 'IVXLCDM'
        reversed_res: str = ''

        i: int
        c: str
        for i, c in enumerate(reversed(str(num))):
            if 1 <= int(c) <= 3:
                reversed_res += symbol[i*2] * int(c)
            elif int(c) == 4:
                reversed_res += (symbol[i*2] + symbol[i*2+1])[::-1]
            elif int(c) == 5:
                reversed_res += symbol[i*2+1]
            elif 6 <= int(c) <= 8:
                reversed_res += (symbol[i*2+1] + symbol[i*2] * (int(c) - 5))[::-1]
            elif int(c) == 9:
                reversed_res += (symbol[i*2] + symbol[i*2+2])[::-1]

        return reversed_res[::-1]
