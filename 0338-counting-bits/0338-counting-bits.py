class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n + 1)
        for i in range(1, n+1):
            res[i] = self.helper(i)
        return res
        
    def helper(self, n):
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count