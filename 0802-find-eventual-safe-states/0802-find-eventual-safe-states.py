from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        reverse_graph = [[] for _ in range(n)]
        outdegree = [0]*n

        # build the reverse graph
        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)
        
        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        safe = [False] * n

        # Kahn's Algorithm
        while queue:
            node = queue.popleft()
            safe[node] = True

            for parent in reverse_graph[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    queue.append(parent)
        return [i for i in range(n) if safe[i]]
        
        