from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])

        visited = [[False]*n for _ in range(m)]
        distance = [[0]*n for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited[i][j]=True
        
        directions =[(1,0), (-1,0), (0,1), (0,-1)]
        #BFS
        while queue:
            x,y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    visited[nx][ny]= True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
        return distance

        