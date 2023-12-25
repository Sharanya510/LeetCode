class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return high +1
        
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                low = mid + 1
                
            if target < nums[mid]:
                high = mid - 1
                
        return high+1