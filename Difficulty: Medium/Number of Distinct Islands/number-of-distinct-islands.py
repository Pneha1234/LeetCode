#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visisted =  [[False]*columns for _ in range(rows)]
        distinct_islands =set()
        
        #create dfs
        def dfs(r,c,base_r, base_c, shape):
            # boundary check
            if r<0 or r>=rows or c<0 or c>=columns:
                return
            if grid[r][c]!= 1 or visisted[r][c]:
                return
            visisted[r][c]= True
            
            #store relevent shape
            shape.append((r-base_r, c-base_c))
            
            #Explore 4 directions:
            dfs(r+1, c, base_r, base_c, shape)
            dfs(r-1, c, base_r, base_c, shape)
            dfs(r, c+1, base_r, base_c, shape)
            dfs(r, c-1, base_r, base_c, shape)
        
        # Traverse the grid
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==1 and not visisted[i][j]:
                    shape= []
                    dfs(i,j, i, j,shape)
                    distinct_islands.add(tuple(shape))
        return len(distinct_islands)