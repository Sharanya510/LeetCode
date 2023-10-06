class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        indegree=[0]*numCourses
        course_map=defaultdict(list)
        
        for preq in prerequisites:
            indegree[preq[0]]+=1
            course_map[preq[1]].append(preq[0])
        # print(indegree)
        # print(course_map)
        
        q=deque()
        
        for i, n in enumerate(indegree):
            if n == 0 :
                q.append(i)
        # print(q)
        while q:
            course=q.popleft()
            for child in course_map[course]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        
        for i in range(len(indegree)):
            if indegree[i]!=0:
                return False
        return True
    
    
    
        