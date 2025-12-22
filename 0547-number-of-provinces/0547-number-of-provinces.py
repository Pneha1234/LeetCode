class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # convert adj maatrix into adj list
        n = len(isConnected)
        adjLs = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adjLs[i].append(j)
        
        visited =set()
        provinces = 0

        # dfs function
        def dfs(city):
            visited.add(city)

            for neighbour in adjLs[city]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        # count number of province
        for city in range(n):
            if city not in visited:
                provinces +=1
                dfs(city)
        return provinces

        