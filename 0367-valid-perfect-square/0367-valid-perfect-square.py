class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for i in range(1, num+1):
        #     product = i * i
        #     if num == product:
        #         return True
        # return False
        
        left, right = 1, num
        while(left <= right):
            mid = (left + right)//2
            product = mid * mid
            if product > num:
                right = mid - 1
            elif product < num:
                left = mid+1
            else:
                return True
        