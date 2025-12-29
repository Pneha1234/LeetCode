

class Solution:
    def isCycle(self, V, edges):
        # create a adj list
        adj =[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # create a visited array
        visited = [False] *V
        
        # create a dfs:
        def dfs(node,parent):
            visited[node]= True
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
            return False
            
        
        # iterate over all the 
        for i in range(V):
            if not visited[i]:
                if dfs(i,-1):
                    return True
        return False
                
