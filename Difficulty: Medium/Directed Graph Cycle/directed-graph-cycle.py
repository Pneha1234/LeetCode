class Solution:
    def isCyclic(self, V, edges):
        # lets build adj list
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        
        # lets build visited and path visited
        visited = [False]*V
        path_visited = [False]*V
        
        #step 3: create a dfs
        # Mark node as visited
        # Mark node as part of current path
        # Visit neighbors
        # If neighbor already in path → cycle found
        # Backtrack (remove from path)
        def dfs(node):
            visited[node] = True
            path_visited[node] = True

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
                elif path_visited[neighbour]:
                    return True

            # Backtrack
            path_visited[node] = False
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
            