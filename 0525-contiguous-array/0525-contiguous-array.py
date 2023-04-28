class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {0:-1}
        length = sum = 0
        for i,n in enumerate(nums):
            if n == 0:
                sum -= 1
            else:
                sum += 1
            if sum in hash:
                length = max(length, i - hash[sum])
            else:
                hash[sum] = i
        return length
        
        
        
#         count = {0: -1}  # Initial count of 0's and 1's
#         max_len = count_diff = 0
        
#         for i, num in enumerate(nums):
#             count_diff += 1 if num == 1 else -1  # Increment count of 1's or 0's
#             if count_diff in count:
#                 max_len = max(max_len, i - count[count_diff])
#             else:
#                 count[count_diff] = i
        
                
                
            
            
        