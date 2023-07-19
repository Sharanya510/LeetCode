class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        hash_set_row , hash_set_col = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    hash_set_row.add(i)
                    hash_set_col.add(j)
        # print(hash_set_row)
        
        for i in range(m):
            for j in range(n):
                if i in hash_set_row or j in hash_set_col:
                    matrix[i][j] = 0
        return matrix