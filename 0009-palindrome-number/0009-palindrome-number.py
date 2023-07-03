class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = 0
        temp = x
        
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //=10
        return reversed_num == x
            
#          121
#         temp = 121
#         digit = 121 % 10 = 1
#         rev 1
#         temp = 121 // 10 = 12
        
#         temp = 12
#         digit = 2
#         rev = 10 + 2 = 12
#         temp = 1
        
#         temp = 1
#         digit = 1
#         rev = 121
#         temp = 0
        