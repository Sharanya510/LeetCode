class Solution:
    def arrangeCoins(self, n: int) -> int:
        #LINEAR-SEARCH
        # rows = 1
        # while (rows < n):
        #     n = n - rows
        #     rows = rows +1
        # return rows-1

        #BINARY-SEARCH
        left, right = 0, n+1
        while left <= right:
            
            middle = (left + right)//2
            
            if (middle*(middle +1))/2 > n:
                right = middle -1
            
            elif (middle*(middle +1))/2 < n:
                left = middle + 1
            
            else:
                return middle
        
        return left-1

        
