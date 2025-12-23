class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # length of row and column
        m = len(grid)
        n = len(grid[0])

        # create exact size replica as grid to trace visited or not
        visited = [[False for _ in range(n)] for _ in range(m)]

        island = 0

        #get horizontal and vertical direction
        directions =[(-1,0), #---> up
                     (1,0), #---> down
                     (0,1), #---> right
                     (0, -1) #----> left
                     ]
        
        #create a queue and start bfs
        def bfs(start_r, start_c):
            queue = []
            visited[start_r][start_c] = True
            queue.append((start_r, start_c))

            while queue:
                r,c = queue.pop(0)

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # boundary check
                    if 0 <= nr < m and 0 <= nc < n:
                        if not visited[nr][nc] and grid[nr][nc] == '1':
                            visited[nr][nc]= True
                            queue.append((nr,nc))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    island +=1
                    bfs(i,j)
        return island





        