class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def helper( n):
            count = 0
            while n != 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count
        
        res = [0] * (n + 1)
        for i in range(1, n+1):
            res[i] = helper(i)
        return res
        # for i in range(0, n+1, 2):
        #     res[i] = helper(i)
        #     res[i+1] = res[i] + 1
        # return res[0:n+1]
        
        