class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1 :
            return False
        
        indegree = [0]*n
        adj_list = defaultdict(list)
        queue = deque()
        
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            
        for edge in edges:
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
            
        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i)
       
        while queue:
            parent = queue.popleft()
            for child in adj_list[parent]:
                indegree[child] -= 1
                if indegree[child] == 1:
                    queue.append(child)
        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True
        
            
        