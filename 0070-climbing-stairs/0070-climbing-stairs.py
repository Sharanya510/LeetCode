class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # a = 1
        # b = 2
        # c = 0
        # for i in range(n-2):
        #     c = a+ b
        #     a = b
        #     b = c
        # return c
        
        x, y = 1, 1
        for i in range(2, n + 1):
            x, y = y, x+ y
        return y
    