class Solution:
    def bfs(self, adj):
        visited =set()
        queue =[]
        result = []
        queue.append(0)
        visited.add(0)
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return result