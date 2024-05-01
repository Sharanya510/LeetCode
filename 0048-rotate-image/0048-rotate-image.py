class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        # print()
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # print(matrix)
       
        for i in range(len(matrix)):
            p1=0
            p2=len(matrix)-1
            while p1<=p2:
                matrix[i][p1],matrix[i][p2]=matrix[i][p2],matrix[i][p1]
                p1+=1
                p2-=1
        return matrix
    
                
        