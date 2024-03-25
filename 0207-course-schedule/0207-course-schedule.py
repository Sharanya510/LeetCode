class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # APPROACH --> DFS
        # TIME COMPLEXITY --> O(M + N)
        # SPACE COMPLEXITY --> O(M + N)
        if not prerequisites:
            return True
        
        indegree = [0]*numCourses
        adjacency_list = defaultdict(list)
        
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            adjacency_list[prereq[1]].append(prereq[0])
            
        queue = deque()
        for index, value in enumerate(indegree):
            if value == 0:
                queue.append(index)
        
        while queue:
            new_value = queue.popleft()
            for child in adjacency_list[new_value]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
        return True
            