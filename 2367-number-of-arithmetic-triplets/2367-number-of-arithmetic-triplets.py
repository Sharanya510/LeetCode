class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        total_triplets = 0
        
        for num in nums:
            if (num + diff in num_set) and (num + 2 * diff in num_set):
                total_triplets += 1
        
        return total_triplets
        
        # total_triplets = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] - nums[i] == diff:
        #             for k in range(j+1, n):
        #                 if nums[k] - nums[j] == diff:
        #                     total_triplets += 1
        # return total_triplets
    
        # total_triplets = 0
        # n = len(nums)
        # for i in range(n - 2):
        #     j = i + 1
        #     k = i + 2
        #     while j < n and k < n:
        #         if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #             total_triplets += 1
        #             j += 1
        #             k += 1
        #         elif nums[j] - nums[i] < diff:
        #             j += 1
        #         elif nums[k] - nums[j] < diff or j == k:
        #             k += 1
        #         else:
        #             j += 1
        #             if j == k:
        #                 k += 1
        # return total_triplets
