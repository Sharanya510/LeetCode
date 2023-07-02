class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # BRUTE FORCE
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             if abs(i-j) <= k:
        #                 return True
        # return False
        
        # nums_hash = {}
        # for i , num in enumerate(nums):
        #     if num not in nums_hash:
        #         nums_hash[num] = i
        #     else:
        #         if abs(i - nums_hash[num]) <= k :
        #             return True
        #         nums_hash[num] = i
        # return False
        
        nums_hash = {}
        for i in range(len(nums)):
            if nums[i] in nums_hash and i - nums_hash[nums[i]] <= k:
                return True
            nums_hash[nums[i]] = i
        return False
        