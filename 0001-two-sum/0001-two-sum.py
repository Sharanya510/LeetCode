class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if num not in hash_map:
                hash_map[diff] = i
            else:
                return [i, hash_map[num]]

            
# i = 0, num = 2, diff = 7
# 7 --> 0
