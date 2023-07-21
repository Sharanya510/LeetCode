class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # hash_map = defaultdict(int)
        # for n in nums:
        #     hash_map[n] += 1
        # for i in hash_map:
        #     if hash_map[i] == 1:
        #         return i

        a = 0
        for i in nums:
            a = a^i
        return a
        