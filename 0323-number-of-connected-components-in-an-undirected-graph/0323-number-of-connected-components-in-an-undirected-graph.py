class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # APPROACH --> BFS
        # TIME COMPLEXITY --> O(E + V) E --> edges, V --> vertices
        # SPACE COMPLEXITY --> O(E + V)
        self.adjacency_list = defaultdict(list)
        self.visited = set()
        count = 0
        for edge in edges:
            self.adjacency_list[edge[0]].append(edge[1])
            self.adjacency_list[edge[1]].append(edge[0])
        # print(self.adjacency_list)
        for node in range(n):
            if node not in self.visited:
                self.visited.add(node)
                count += 1
                self.bfs(node)
        return count
    
    def bfs(self, node):
        queue= deque()
        queue.append(node)
        while queue:
            parent = queue.popleft()
            for child in self.adjacency_list[parent]:
                if child not in self.visited:
                    self.visited.add(child)
                    queue.append(child)
        
        