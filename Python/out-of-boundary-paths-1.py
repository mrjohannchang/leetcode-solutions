class Solution:
    def findPaths(self, m: int, n: int, max_move: int, start_row: int, start_column: int) -> int:
        highest_move_dictionary: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        highest_move_dictionary[start_row][start_column] = 1

        count: int = 0

        if max_move == 0:
            return count

        for _ in range(max_move):
            current_move_dictionary: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
            i: int
            for i in range(m):
                j: int
                for j in range(n):
                    if i == 0:
                        count += highest_move_dictionary[i][j]
                    if i == m - 1:
                        count += highest_move_dictionary[i][j]
                    if j == 0:
                        count += highest_move_dictionary[i][j]
                    if j == n - 1:
                        count += highest_move_dictionary[i][j]
                    c: int = 0
                    if i > 0:
                        c += highest_move_dictionary[i-1][j]
                    if i < m - 1:
                        c += highest_move_dictionary[i+1][j]
                    if j > 0:
                        c += highest_move_dictionary[i][j-1]
                    if j < n - 1:
                        c += highest_move_dictionary[i][j+1]
                    current_move_dictionary[i][j] = c
            highest_move_dictionary = current_move_dictionary
        return count % (10**9 + 7)
