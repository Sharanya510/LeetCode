class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for n in nums:
            hash_table[n] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i
        