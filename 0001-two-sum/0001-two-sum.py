class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if n not in nums_map:
                nums_map[diff] = i
            else:
                return [i, nums_map[n]]
                
                
                
            
                
                

            