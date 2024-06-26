class Solution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents
