class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[high] > nums[low]:
            return nums[low]
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid ] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        
          