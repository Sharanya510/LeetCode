class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[low] < nums[high]:
            return nums[low]
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid + 1] and nums[mid - 1] > nums[mid] :
                return nums[mid]
            elif nums[low] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
            
            
            


