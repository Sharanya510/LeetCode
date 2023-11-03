class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return self.helper(source, destination, adj_list, visited)
    
    def helper(self, source, destination, adj_list, visited):
        if source == destination:
            return True
        if source not in visited:
            visited.add(source)
            for child in adj_list[source]:
                if self.helper(child, destination, adj_list, visited):
                    return True
        return False
                