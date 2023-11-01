class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            n = self.keep_dividing_when_divisible(n, factor)
        return n == 1
    
    def keep_dividing_when_divisible(self,dividend, divisor):
        while dividend % divisor == 0:
            dividend //= divisor
            print(dividend)
        return dividend

        # Check if the integer is reduced to 1 or not.
       
            
        