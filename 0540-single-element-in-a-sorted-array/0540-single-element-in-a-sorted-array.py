class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1   
        while low < high:
            mid = low + (high - low) // 2
            halves_are_even = (high - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]
        
# 0   1   2   3   4   5   6   7   8  
# 1   1   2   3   3   4   4   8   8
# l               m               h   m = 4     halves = true
# check if mid and mid + 1 are equal, 
#       if yes, then check if right_halves is true, 
#           if yes, then the single element will be on the right side, 
#           else it will be on the left side
# else check if mid and mid - 1 are equal,
#       if yes, then check if right_halves is true
#           if yes, then the single element will be on the left side,
#           else it will be on the right side
# else the middle element itself is the single element
#   so return middle element
        
        # BRUTE--FORCE
        # for i in range(0, len(nums) - 2, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]
            
        