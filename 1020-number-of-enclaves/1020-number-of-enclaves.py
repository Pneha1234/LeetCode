from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        visited = [[False] * column for _ in range(row)]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= column:
                return
            if grid[r][c] != 1 or visited[r][c]:
                return

            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1️⃣ Run DFS from boundary cells
        for c in range(column):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[row - 1][c] == 1:
                dfs(row - 1, c)

        for r in range(row):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][column - 1] == 1:
                dfs(r, column - 1)

        # 2️⃣ Count unvisited land cells
        counter = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and not visited[i][j]:
                    counter += 1

        return counter
