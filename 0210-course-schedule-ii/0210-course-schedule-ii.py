from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create the adj list
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] +=1


        # Step 2: Queue for courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # step 3 Kahn's algorithm
        order = []
        while queue:
            courses = queue.popleft()
            order.append(courses)

            for neighbours in adj[courses]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
        
        # if cycle exists, topo sort not possible
        if len(order) != numCourses:
            return []
        return order


        