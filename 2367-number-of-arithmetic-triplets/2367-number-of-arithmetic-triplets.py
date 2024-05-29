class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        total_triplets = 0
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = i + 2
            while j < n and k < n:
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    total_triplets += 1
                    j += 1
                    k += 1
                elif nums[j] - nums[i] < diff:
                    j += 1
                elif nums[k] - nums[j] < diff or j == k:
                    k += 1
                else:
                    j += 1
                    if j == k:
                        k += 1
        return total_triplets
