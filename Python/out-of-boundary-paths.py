class Solution:
    def __init__(self):
        self.dictionary: list[list[list[int]]] = [[[-1 for _ in range(50)] for _ in range(50)] for _ in range(51)]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        if maxMove == 0:
            return 0
        if self.dictionary[maxMove][startRow][startColumn] >= 0:
            return self.dictionary[maxMove][startRow][startColumn]
        self.dictionary[maxMove][startRow][startColumn] = sum([
            self.findPaths(m, n, maxMove-1, startRow-1, startColumn),
            self.findPaths(m, n, maxMove-1, startRow+1, startColumn),
            self.findPaths(m, n, maxMove-1, startRow, startColumn-1),
            self.findPaths(m, n, maxMove-1, startRow, startColumn+1)]) % (10**9 + 7)
        return self.dictionary[maxMove][startRow][startColumn]
