class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * n
        queue = deque()
        adj_list = defaultdict(list)
        
        for relation in relations:
            indegree[relation[1] - 1] += 1
            adj_list[relation[0]].append(relation[1])
        # print(indegree)
        # print(adj_list)
        
        res = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i+1)
                
        while queue:
            size = len(queue)
            res += 1
            for i in range(size):
                parent = queue.popleft()
                for child in adj_list[parent]:
                    indegree[child - 1] -= 1
                    if indegree[child - 1] == 0:
                        queue.append(child)
        
        for i in range(1, len(indegree)):
            if indegree[i] != 0:
                return -1
            else:
                return res
        
        