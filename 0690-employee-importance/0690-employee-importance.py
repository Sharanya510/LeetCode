"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list={}
        queue=deque()
        res=0
        queue.append(id)
        
        for employee in employees:
            adj_list[employee.id] = (employee.importance, employee.subordinates)
        
        while queue:
            node=queue.popleft()
            node_values=adj_list[node]
            res+=node_values[0]
            
            for child in node_values[1]:
                queue.append(child)
                
        return res
        
        