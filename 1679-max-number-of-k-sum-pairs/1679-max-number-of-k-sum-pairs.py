class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = 0
        nums.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == k:
                length += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] > k:
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
        return length