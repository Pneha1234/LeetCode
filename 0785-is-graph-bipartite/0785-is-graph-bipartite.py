from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color = [-1] *n

        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        queue.append(neighbour)
                    elif color[neighbour] == color [node]:
                        return False
        return True
