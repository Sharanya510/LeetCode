class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(i):
            if i in visited: return 0
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    dfs(j)
            return 1

        provinces = 0

        for i in range(len(isConnected)):
            provinces += dfs(i)

        return provinces