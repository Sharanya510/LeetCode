class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum, current_sum = 0, 0
        for i in range(k):
            current_sum += nums[i]
        maxsum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            maxsum = max(maxsum, current_sum)
        return maxsum/k