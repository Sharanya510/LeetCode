class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left , right = 0, len(nums)-1
        while(left <= right):
            mid = (left + right) //2
            if target == nums[mid] or nums[left] == target or nums[right] == target:
                return True
            elif nums[mid] == nums[left] == nums[right]:
                left = left + 1
                right = right - 1
            
            #left-sided portion
            elif nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            #right-sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
        