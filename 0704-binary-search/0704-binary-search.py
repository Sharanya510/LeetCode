class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        return self.helper(start, end, nums, target)
            
         
        
    def helper(self, start, end, nums, target):
        if start > end:
            return -1
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        mid = (start + end) //2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.helper(mid+1, end, nums, target)
        else:
            return self.helper(start, mid-1, nums, target)
        
        