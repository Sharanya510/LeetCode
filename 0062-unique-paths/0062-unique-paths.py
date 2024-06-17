class Solution(object):
    def uniquePaths(self, m, n):
        visited=set()
        hash_map={}
        return self.helper(0,0,visited,m,n,hash_map)
    
    def givestr(self, i, j):
        return str(i)+ ", "+str(j)
    def helper(self,i,j,visited,m,n,hash_map):
        if i==m-1 and j==n-1:
            return 1
        if self.givestr(i,j) in hash_map:
            return hash_map[self.givestr(i,j)]
        directions=[[0,1],[1,0]]
        visited.add((i,j))
        # print("i am here")
        count=0
        for dirs in directions:
            new_i=dirs[0]+i
            new_j=dirs[1]+j
            if new_i>=0 and new_j>=0 and new_i<m and new_j<n and (new_i,new_j) not in visited:
                count+=self.helper(new_i,new_j,visited,m,n,hash_map)
        # remove
        visited.remove((i,j))
        hash_map[self.givestr(i,j)]=count
        return count
        
    
    
    
        
                    
                
            
        