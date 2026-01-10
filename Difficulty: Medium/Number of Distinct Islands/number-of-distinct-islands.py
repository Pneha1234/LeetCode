#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        row,coloumn = len(grid), len(grid[0])
        visited = [[False]*coloumn for _ in range(row)]
        unique_shape =set()

        def dfs(r,c, base_r, base_c, shape):
            # check boundary
            if r < 0 or r>= row or c < 0 or c >= coloumn:
                return 
            if grid[r][c] !=1 or visited[r][c]:
                return
            visited[r][c]=True
            shape.append((r -base_r, c-base_c))
            dfs(r+1,c,base_r,base_c, shape)
            dfs(r-1,c,base_r, base_c, shape)
            dfs(r,c+1,base_r, base_c, shape)
            dfs(r,c-1,base_r,base_c, shape)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visited[i][j]:
                    shape = []
                    dfs(i,j,i,j, shape)
                    unique_shape.add(tuple(shape))
        return len(unique_shape)