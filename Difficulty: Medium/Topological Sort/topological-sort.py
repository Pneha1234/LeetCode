class Solution:
    def topoSort(self, V, edges):
        # step 1: create adjaceny list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        visited = [False]*V
        stack = []
        
        # step 2: created dfs
        def dfs(node):
            visited[node]= True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            
            # push to stack
            stack.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        return stack[::-1]
            
                    