from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # step 1: create adjaceny list
        # adj = [[] for _ in range(V)]
        # for u, v in edges:
        #     adj[u].append(v)
            
        # visited = [False]*V
        # stack = []
        
        # # step 2: created dfs
        # def dfs(node):
        #     visited[node]= True
        #     for neighbour in adj[node]:
        #         if not visited[neighbour]:
        #             dfs(neighbour)
            
        #     # push to stack
        #     stack.append(node)
            
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i)
        
        # return stack[::-1]
        
        # Kahn's algorithm
        # Step1 : build adjaceny matrix
        adj = [[] for _ in range(V)]
        indegree = [0]*V
        
        for u,v in edges:
            adj[u].append(v)
            indegree[v] +=1
        
        # step 2 : push nodes with indegree 0 in queue
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        topo_order = []
        
        # start bfs
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return topo_order
        
        
            
                    