class Solution:
    def climbStairs(self, n: int) -> int:
        # using DP
        # one, two = 1, 1
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        # return one
        # using fibonacci series approach
        k1 = 0
        k2 = 1
        while n > 0:
            k1, k2 = k2, k1+k2
            n-= 1
        return k2
        
            
            
            
            
        