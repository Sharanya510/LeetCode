class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        for num in arr:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for i in hash_map.values():
            return len(set(hash_map.values())) == len(hash_map.values())
            