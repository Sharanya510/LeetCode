class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        S = Counter(s)
        if len(s) == 0 or k > len(s): return 0
        sub1, sub2 = 0, 0
        for i, ele in enumerate(s):
            if S[ele] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
        
        
        
        
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