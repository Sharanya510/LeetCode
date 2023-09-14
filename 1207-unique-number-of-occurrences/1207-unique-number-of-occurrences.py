class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        for n in arr:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                hash_map[n] += 1
        hash_set = set()
        for key, value in hash_map.items():
            if value not in hash_set:
                hash_set.add(value)
            else:
                return False
        return True