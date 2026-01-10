from collections import deque

class Solution:
    def isBipartite(self, V, edges):
        color = [-1]*V
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        queue = deque()
        
        for i in range(V):
            if color[i] == -1:
                queue.append(i)
                color[i]=1
                
                while queue:
                    node = queue.popleft()
                    for neighbour in adj[node]:
                        if color[neighbour] == -1:
                            color[neighbour] = 1- color[node]
                            queue.append(neighbour)
                        elif color[neighbour] == color[node]:
                            return False
        return True
                
        