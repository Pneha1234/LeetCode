class Solution:
    def dfs(self, adj):
        result = []
        # code here
        visited_array = [False] * len(adj)
        def dfs_internal(node, visited_array):
            for neighbour in adj[node]:
                if not visited_array[neighbour]:
                    visited_array[neighbour] = True
                    result.append(neighbour)
                    dfs_internal(neighbour, visited_array)
        visited_array[0]=True
        result.append(0)
        dfs_internal(0, visited_array)
        return result