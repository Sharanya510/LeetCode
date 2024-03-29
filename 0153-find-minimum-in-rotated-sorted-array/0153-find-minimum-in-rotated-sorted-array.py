class Solution:
    def findMin(self, nums: List[int]) -> int:
        # APPROACH --> BINARY SEARCH
        # TIME COMPLEXITY --> O(LOG N)
        # SPACE COMPLEXITY --> O(1)
        low, high = 0, len(nums)-1
        if nums[low] < nums[high]:
            return nums[low]
        if len(nums) == 1:
            return nums[0]
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[high] and nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid +1
            
            
            
            
            

        