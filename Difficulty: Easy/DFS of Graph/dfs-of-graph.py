class Solution:
    def dfs(self, adj):
        # adjacency list
        # step 1: To find the length of graph
        # number of vertices = length of adjacency list
        V = len(adj)
        visited_node = [False]*V
        result =[]
        
        def dfs_recursion(node):
            visited_node[node] = True
            result.append(node)
            
            for neighbour in adj[node]:
                if not visited_node[neighbour]:
                    dfs_recursion(neighbour)
            
        # start DFS from vertex 0
        dfs_recursion(0)
        return result
        