class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedXor = 0
        actualXor = 0
        for i in range(len(nums)+1):
            expectedXor ^= i
        
        for num in nums:
            actualXor ^= num
        
        return expectedXor ^ actualXor
        
        
        # res=0
        # for i in range(1, len(nums)+1):
        #     print("res value before: ", res)
        #     res = res ^ i
        #     print("res value after i value: ", res)
        #     res = res ^ nums[i-1]
        #     print("res value after nums iteration: ", res)
        # return res
        
#         hash_set = set(nums)
#         n = len(nums)+1
        
#         for i in range(n):
#             if i not in hash_set:
#                 return i
    
        # 0 or 0 = 0
        # 0 xor 0 = 0
        
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i]!=i:
        #         return i
        # return len(nums)
        
        # 11 xor 01 = 10