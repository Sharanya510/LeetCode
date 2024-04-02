class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        indegree = [0]*n
        adj_list = defaultdict(list)
        group_A = set()
        group_B = set()
        
        for dislike in dislikes:
            adj_list[dislike[0]].append(dislike[1])
            adj_list[dislike[1]].append(dislike[0])
        
        color = [-1] * (n+1)
        for i in range(1, n+1):
            if color[i] == -1:
                if not self.bfs(i, color, adj_list):
                    return False
        return True
    
    def bfs(self, source, color, adj_list):
        queue = deque()
        queue.append(source)
        color[source] = 0
        
        while queue:
            node = queue.popleft()
        
            for neighbor in adj_list[node]:
                if color[neighbor] == color[node]:
                    return False
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
        return True
                
                
        