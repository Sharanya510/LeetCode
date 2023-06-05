class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute-Force
        # nums = sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1] :
        #         return True
        # return False
        
        #one-line solution
        return len(set(nums)) != len(nums)
        
               