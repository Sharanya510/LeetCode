class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = Counter()
        for elem in candidates:
            i = 0
            while elem:
                if elem % 2 == 1:
                    result[i] += 1
                elem //= 2
                i += 1
        return max(result.values())