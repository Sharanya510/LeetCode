class Solution:
    def shareSameRowOrColumn(self, a, b):
        return a[0] == b[0] or a[1] == b[1]

    def dfs(self, stones, adj, visited, src):
        visited.add(src)
        for adjacent in adj[src]:
            if adjacent not in visited:
                self.dfs(stones, adj, visited, adjacent)

    def removeStones(self, stones):
        adj = defaultdict(list)
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if self.shareSameRowOrColumn(stones[i], stones[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        visited = set()
        componentCount = 0
        for i in range(len(stones)):
            if i not in visited:
                componentCount += 1
                self.dfs(stones, adj, visited, i)
        return len(stones) - componentCount
