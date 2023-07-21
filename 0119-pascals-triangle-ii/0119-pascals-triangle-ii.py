class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        res.append([1])
        for i in range(rowIndex):
            firstrow = [1]
            for j in range(i):
                firstrow.append(res[i][j]+res[i][j+1])
            firstrow.append(1)
            res.append(firstrow)
        return res[rowIndex]
        