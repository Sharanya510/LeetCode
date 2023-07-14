class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,  high = 0, len(nums) - 1
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        
        if target == nums[low]:
            return low
        if target == nums[high]:
            return high
        
        while low <= high :
            mid = (low + high) // 2
            
            if nums[mid] == target :
                return mid
            
            if nums[mid] >= nums[low] :
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
                
                    
# 4   5   6   7   0   1   2
# l           m           h
                #  l    m     h
                # l h
                    

                