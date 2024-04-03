class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxRobbedAmount = [None]*(len(nums) + 1)
        N = len(nums)
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
        return maxRobbedAmount[0]  
    
        # even_sum, odd_sum = 0, 0
        # for i in range(0, len(nums), 2):
        #     even_sum += nums[i]
        # for j in range(1, len(nums), 2):
        #     odd_sum += nums[j]
        # res = max(even_sum, odd_sum)
        # return res