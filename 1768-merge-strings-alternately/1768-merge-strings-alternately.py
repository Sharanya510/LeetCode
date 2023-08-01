class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # ONE POINTER
        res = ""
        length = max(len(word1), len(word2))
        
        for i in range(length):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res
        
        
        
#         TWO POINTERS
#         m = len(word1)
#         n = len(word2)
#         i = 0
#         j = 0
#         res = ""
        
#         while i < m or j < n:
#             if i < m:
#                 res += word1[i]
#                 i += 1
#             if j < n:
#                 res += word2[j]
#                 j += 1
#         return res