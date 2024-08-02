class Solution:
    def __init__(self):
        self.count = 0
    
    def bfs(self, node, n, adj):
        q = deque()
        visit = [False] * n
        q.append(node)
        visit[node] = True

        while q:
            node = q.popleft()
            for neighbor, sign in adj[node]:
                if not visit[neighbor]:
                    self.count += sign
                    visit[neighbor] = True
                    q.append(neighbor)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], 0))
        self.bfs(0, n, adj)
        return self.count