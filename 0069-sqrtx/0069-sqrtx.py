class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid*mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
                
        return high
        
        
# 0   1   2   3   4   5   6   7   8
# mid = 0 + 8 // 2 = 4
# mid*mid > target --> 4 > 8 --> left side
# else right side
# 0   1   2   3 
# 1 * 1 < target --> move to right side

# 2   3
# mid = 2
# 2 * 2 < target --> right side
# 3 * 3 > target --> left side


# 0   1   2   3   4   5   6
# mid = 3
# 9 > 6 --> left side
# 0   1   2
# mid = 1
# 1 < 6 --. right side
# 2
# 4 < 6 


            
        