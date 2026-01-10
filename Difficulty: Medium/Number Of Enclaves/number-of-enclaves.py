#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        visited = [[False]* column for _ in range(row)]
        number_of_enclave = 0
        
        def dfs(r,c):
            if r < 0 or r >=row or c < 0 or c >= column:
                return
            if grid[r][c] !=1 or visited[r][c]:
                return
            visited[r][c] = True
            
            # run dfs on all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        
        # run over boundary
        for c in range(column):
            if grid[0][c] == 1:
                dfs(0,c)
            if grid[row-1][c] ==1:
                dfs(row-1,c)
        
        # run over row boundary
        for r in range(row):
            if grid[r][0] ==1:
                dfs(r, 0)
            if grid[r][column-1]==1:
                dfs(r, column-1)
        
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 and not visited[r][c]:
                    number_of_enclave +=1
        return number_of_enclave