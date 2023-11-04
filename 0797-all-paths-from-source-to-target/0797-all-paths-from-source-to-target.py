class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = {}
        n = len(graph)
        for index, edge in enumerate(graph):
            adj_list[index] = edge
        visited=set()
        res=[]
        temp=[]
        self.helper(0, adj_list,res,temp,n)
        return res
    
    def helper(self,source,adj_list,res,temp,n):
        temp.append(source)
        if source==n-1:
            res.append(list(temp))
            temp.pop()
            return
        for child in adj_list[source]:
            self.helper(child,adj_list,res,temp,n)
        temp.pop()
        
        
        
        