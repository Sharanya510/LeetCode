class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]* n
        outdegree = [0] * n
        
        if n == 1 and not trust:
            return n
        
        for item in trust:
            indegree[item[1]-1] += 1
            outdegree[item[0]-1] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i + 1
        return -1
        