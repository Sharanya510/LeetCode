class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque()
        queue.append([0])
        adj_list = {}
        res = []
        n = len(graph)
        for index, edge in enumerate(graph):
            adj_list[index] = edge
        
        visited = set()
        visited.add(0)
        
        while queue:
            parent = queue.popleft()
            if parent[-1] == n-1:
                res.append(parent)
            for child in adj_list[parent[-1]]:
                queue.append(parent+[child])
        return res
                
                