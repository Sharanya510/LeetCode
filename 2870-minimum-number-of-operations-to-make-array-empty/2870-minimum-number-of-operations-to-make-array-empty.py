class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_hashmap = Counter(nums)
        count = 0
        for key, value in nums_hashmap.items():
            if value < 2:
                return -1
            # count += min(value // 2 + value % 2, value // 3 + value % 3)
            count += min(ceil(value / 2) , ceil(value / 3) )
        return count
    
# 5 // 2 + 5 % 2 --> 2 + 1 = 3
# 5 // 3 + 5 % 3 --> 1 + 2 = 3