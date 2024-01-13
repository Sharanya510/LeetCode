class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
        # nums_set = set(nums)
        # return len(nums) != len(nums_set)
    #TIME COMPLEXITY --> O(1)
    #SPACE COMPLEXITY --> O(n)
    