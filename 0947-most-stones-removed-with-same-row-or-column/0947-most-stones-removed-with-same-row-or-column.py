class Solution:
    def shareSameRowOrColumn(self, a, b):
        # Return true if stone a and b shares row or column
        return a[0] == b[0] or a[1] == b[1]

    def dfs(self, stones, adj, visited, src):
        # Mark the stone as visited
        visited[src] = 1
        
        # Iterate over the adjacent, and recurse over it if not visited yet
        for adjacent in adj[src]:
            if visited[adjacent] == 0:
                self.dfs(stones, adj, visited, adjacent)

    def removeStones(self, stones):
        # Adjacency list to store edges
        adj = [[] for _ in stones]
        
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if self.shareSameRowOrColumn(stones[i], stones[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        
        # Array to mark visited stones
        visited = [0] * len(stones)
        # Counter for connected components
        componentCount = 0
        for i in range(len(stones)):
            if visited[i] == 0:
                # If the stone is not visited yet,
                # Start the DFS and increment the counter
                componentCount += 1
                self.dfs(stones, adj, visited, i)
        
        # Return the maximum stones that can be removed
        return len(stones) - componentCount
