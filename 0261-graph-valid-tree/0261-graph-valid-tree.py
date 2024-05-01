class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # APPROACH --> BFS
        # TIME COMPLEXITY --> O(E + N), E --> EDGES, n --> NODES
        # SPACE COMPLEXITY --> O(E + N)
        if len(edges) != n - 1:
            return False
        indegree = [0]*n
        adjacency_list = defaultdict(list)
        queue = deque()
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i)
        # print(queue)
        while queue:
            parent = queue.popleft()
            for child in adjacency_list[parent]:
                indegree[child] -= 1
                if indegree[child] == 1:
                    queue.append(child)
                    
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True