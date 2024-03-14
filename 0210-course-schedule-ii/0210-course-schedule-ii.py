class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        if not prerequisites:
            for i in range(numCourses-1, -1, -1):
                res.append(i)
            return res
        
        indegree = [0]*numCourses
        adjacency_list = defaultdict(list)
        
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            adjacency_list[prereq[1]].append(prereq[0])
            
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                res.append(i)
                
        while queue:
            new_value = queue.popleft()
            for child in adjacency_list[new_value]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    res.append(child)
        
        # Check if there's any remaining course with indegree not equal to 0
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
        return res
        