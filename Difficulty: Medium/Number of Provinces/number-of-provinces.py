class Solution:
    def numProvinces(self, adj, V):
        visited = [False] * V
        province_count = 0

        def dfs(node):
            visited[node] = True
            for neighbour in range(V):
                if adj[node][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        for i in range(V):
            if not visited[i]:
                province_count += 1
                dfs(i)

        return province_count