class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute-Force
        # nums = sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1] :
        #         return True
        # return False
        
        #one-line solution
        # return len(set(nums)) != len(nums)
        
        #using a set DS
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)
        return False
                
        
        
               