from collections import deque

class Solution:
    def isCycle(self, V, edges):
        # Step 1: Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Visited array
        visited = [False] * V

        # Step 3: BFS for each component
        for start in range(V):
            if not visited[start]:
                queue = deque()
                queue.append((start, -1))
                visited[start] = True

                while queue:
                    node, parent = queue.popleft()

                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append((neighbor, node))
                        elif neighbor != parent:
                            return True  # Cycle found

        return False
