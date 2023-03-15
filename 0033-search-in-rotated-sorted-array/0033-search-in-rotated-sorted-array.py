class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #LINEAR SEARCH
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
            
        #BINARY SEARCH
        left, right = 0, len(nums) - 1
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            
            #Left-sorted portion
            if nums[left]<=nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid +1
                else:
                    right = mid - 1
            
            #right-sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1
                

                
            
            
            
