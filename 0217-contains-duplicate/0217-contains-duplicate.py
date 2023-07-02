class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # BRUTE -- FORCE
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
                
        #SORTING
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        #USING COUNTER FUNCTION
        # freq = Counter(nums)
        # for num, freq in freq.items():
        #     if freq > 1:
        #         return True
        # return False
        
        #HASHMAP
        nums_hash = {}
        for num in nums:
            if num not in nums_hash:
                nums_hash[num] = 0
            nums_hash[num] += 1
        for num, freq in nums_hash.items():
            if freq > 1:
                return True
        return False