class Solution:
    def reverse(self, x: int) -> int:
        reversed_number = 0
        
        while x > 0:
            remainder = x % 10
            reversed_number = reversed_number * 10 + remainder
            x = x // 10
        reversed_number = reversed_number
        
        if x < 0:
            x = abs(x)
            while x > 0:
                remainder = x % 10
                reversed_number = reversed_number * 10 + remainder
                x = x // 10
            reversed_number = -1 * reversed_number
        
        if -2**31 <= reversed_number <= 2**31 - 1:
            res = reversed_number
        else:
            res = 0
        return res