class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(set)
        for u, v in edges:
            visited = set()
            if u in self.graph and v in self.graph and self.dfs(u, v, visited):
                return u, v
            self.graph[u].add(v)
            self.graph[v].add(u)
            
    def dfs(self, source, target, visited):
            if source not in visited:
                visited.add(source)
                if source == target: return True
                return any(self.dfs(neighbour, target, visited) for neighbour in self.graph[source])