class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = deque()
        queue.append(source)
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        visited.add(source)
        while queue:
            parent = queue.popleft()
            if parent == destination:
                return True
            for child in adj_list[parent]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
        return False
        