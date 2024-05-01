class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        N=len(nums)
        min_value = max_index = nums[0]
        min_index = max_value = 0
        for i, num in enumerate(nums):
            if num < min_value:
                min_index = i
                min_value = num
            if num >= max_value:
                max_index = i
                max_value = num
        count=0
        if max_index<min_index:
            #count=min_index-max_index+N-1-min_index+max_index
            count = N - 1 - max_index + min_index -1
        else:
            count = min_index + N - 1 - max_index
        return count
            
            
            
#             3 4 5 5 3 1 2
#             0 1 2 3 4 5 6
            
              # 3 4 5 1 3   5
              #       3   5
#             5-3+0+3=6
            
            
            
            
            
#             3 1 5 4 2
#             0 1 2 3 4
            
    
    