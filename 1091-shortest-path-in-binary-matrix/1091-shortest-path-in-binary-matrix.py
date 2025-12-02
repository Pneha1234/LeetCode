class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # step 1:check the length of grid, for boundary check
        n= len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        
        # predefined direction matrix
        directions=[(-1,-1), (-1, 0), (-1,1),
                    (0,-1),            (0,1),
                    (1,-1),    (1,0),   (1,1)]
        
        #create visited array:
        visited = [[False]*n for _ in range(n)]
        visited[0][0]=True

        #queue
        queue =[]
        queue.append((0,0,1))

        while len(queue)>0:
            row, column , dist = queue.pop(0)
            if row == n-1 and column == n-1:
                return dist

            for dr, dc in directions:
                nr = row + dr
                nc = column +dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))
        return -1
