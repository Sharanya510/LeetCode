class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
#         OPTIMIZED
        first_smallest = float("inf")
        second_smallest = float("inf")
        for num in nums:
            if num <= first_smallest:
                first_smallest = num
            elif num > first_smallest and num <= second_smallest:
                second_smallest = num
            elif num > first_smallest and num > second_smallest:
                return True
        return False
        
        
        
        
        
        
        
        
        # BRUTE-FORCE
        # n = len(nums)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True
        # return False
        # i, j, k = 0, 1, 2
        # n = len(nums)
        # while i < n and j < n and k < n:
        #     if i<j and j< k:
        #         if nums[i] < nums[j] and nums[j] < nums[k]:
        #             return True
        #         elif nums[i] < nums[j] and nums[j] > nums[k]:
        #             j += 1
        #             k += 1
        #         elif nums[i] > nums[j] and nums[j] < nums[k]:
        #             i += 1
        #             j += 1
        #             k +=1
                    
# 20  100 10  12  5   13
#  i    j 
# 
# 
# 
# 
# 
        