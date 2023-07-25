class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        
        while columnNumber != 0:
            temp1, temp2 = 0,0
            columnNumber = columnNumber - 1
            
            temp1 = columnNumber % 26
          
            columnNumber = columnNumber // 26
            
            temp2 = temp1 + 65
            
            res += chr(temp2)
            
        return res[::-1]
       
            
        