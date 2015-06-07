# -*- coding: utf-8 -*-

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        grid = [list(map(int, iter(r))) for r in grid]
        if not grid:
            return 0
        res = 0
        travesed = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    continue
                if r in travesed and c in travesed[r]:
                    continue
                res += 1
                travesed.setdefault(r, set())
                travesed[r].add(c)
                q = []
                if r - 1 >= 0 and grid[r-1][c]:
                    q.append([r - 1, c])
                if r + 1 < len(grid) and grid[r+1][c]:
                    q.append([r + 1, c])
                if c - 1 >= 0 and grid[r][c-1]:
                    q.append([r, c - 1])
                if c + 1 < len(grid[0]) and grid[r][c+1]:
                    q.append([r, c + 1])
                while q:
                    rr, cc = q[0][0], q[0][1]
                    if not (rr in travesed and cc in travesed[rr]):
                        travesed.setdefault(rr, set())
                        travesed[rr].add(cc)
                        if rr - 1 >= 0 and grid[rr-1][cc]:
                            q.append([rr - 1, cc])
                        if rr + 1 < len(grid) and grid[rr+1][cc]:
                            q.append([rr + 1, cc])
                        if cc - 1 >= 0 and grid[rr][cc-1]:
                            q.append([rr, cc - 1])
                        if cc + 1 < len(grid[0]) and grid[rr][cc+1]:
                            q.append([rr, cc + 1])
                    q.pop(0)
        return res
