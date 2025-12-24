class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols =  len(grid), len(grid[0])
        queue = []
        fresh_oranges = 0

        # scan the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges +=1
        # case when we have no fresh oranges
        if fresh_oranges == 0:
            return 0
        
        minutes = 0
        direction = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            size = len(queue)
            changed = False

            for _ in range(size):
                r,c = queue.pop(0)

                # find new direction
                for dr, dc in direction:
                    nr, nc = r+ dr, c+dc

                    # check the boundary
                    if 0 <= nr < rows and  0 <= nc < cols and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc] =2
                        fresh_oranges -=1
                        changed = True
            if changed:
                minutes +=1
        return minutes if fresh_oranges == 0 else -1




        