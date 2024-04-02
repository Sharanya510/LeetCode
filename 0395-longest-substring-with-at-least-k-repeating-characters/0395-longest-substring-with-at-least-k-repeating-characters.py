class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def getMaxUniqueLetters(s):
            return len(set(s))

        maxUnique = getMaxUniqueLetters(s)
        result = 0
        for currUnique in range(1, maxUnique + 1):
            # Reset countMap
            countMap = [0] * 26
            windowStart, windowEnd = 0, 0
            unique, countAtLeastK = 0, 0
            while windowEnd < len(s):
                # Expand the sliding window
                if unique <= currUnique:
                    idx = ord(s[windowEnd]) - ord('a')
                    if countMap[idx] == 0:
                        unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k:
                        countAtLeastK += 1
                    windowEnd += 1
                # Shrink the sliding window
                else:
                    idx = ord(s[windowStart]) - ord('a')
                    if countMap[idx] == k:
                        countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0:
                        unique -= 1
                    windowStart += 1
                if unique == currUnique and unique == countAtLeastK:
                    result = max(windowEnd - windowStart, result)
        return result
        
        
        
        
        
#         APPROACH --> BRUTE FORCE
#         if not s or k > len(s):
#             return 0
#         result = 0
#         n = len(s)
#         for start in range(n):
#             countMap = [0] * 26
#             for end in range(start, n):
#                 countMap[ord(s[end]) - ord('a')] += 1
#                 if self.isValid(s, start, end, k, countMap):
#                     result = max(result, end - start + 1)
#         return result

#     def isValid(self, s, start, end, k, countMap):
#         countLetters = 0
#         countAtLeastK = 0
#         for freq in countMap:
#             if freq > 0:
#                 countLetters += 1
#             if freq >= k:
#                 countAtLeastK += 1
#         return countAtLeastK == countLetters