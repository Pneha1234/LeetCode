class Solution:
    def fill(self, grid):
        row , column = len(grid), len(grid[0])
        visited = [[False]* column for _ in range(row)]
        
        def dfs(r,c):
            # boumndary check
            if r < 0 or r >= row or c< 0 or c >= column:
                return
            if grid[r][c] != 'O' or visited[r][c]:
                return
            visited[r][c]= True
            
            # dfs in all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        
        # loop over grid boundary and figure out '0'
        for c in range(column):
            if grid[0][c] == 'O':
                dfs(0,c)
            if grid[row-1][c] == 'O':
                dfs(row-1,c)
        
        for r in range(row):
            if grid[r][0] == 'O':
                dfs(r,0)
            if grid[r][column-1] == 'O':
                dfs(r, column-1)
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 'O' and not visited[r][c]:
                    grid[r][c] = 'X'
        
        