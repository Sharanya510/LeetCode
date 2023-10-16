class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in hashmap:
                hashmap[n] = i
            else:
                return [i, hashmap[diff]]