class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        completed = 0
        while queue:
            courses = queue.popleft()
            completed +=1

            for neighbours in adj[courses]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
        
        
        return completed == numCourses
        