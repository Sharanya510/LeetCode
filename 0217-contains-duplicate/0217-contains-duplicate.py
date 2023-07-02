class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # BRUTE -- FORCE
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
                
        #SORTING
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        #USING COUNTER FUNCTION
        freq = Counter(nums)
        for num, freq in freq.items():
            if freq > 1:
                return True
        return False
        
        
        
        
        # nums_hash = {}
        # for i, n in enumerate(nums):
        #     if n not in nums_hash:
        #         nums[i] += n
        #     elif nums[i] >= 2:
        #         return True
        # return False