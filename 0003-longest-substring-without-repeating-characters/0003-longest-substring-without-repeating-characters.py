class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1
        
        if len(s) == 0:
            return 0
        for i in range(len(s)-1):
            length = 1
            for j in range(i + 1, len(s)):
                if s[j] not in s[i:j]:
                    length += 1
                else:
                    break
                max_length = max(length,  max_length)
            
        return max_length
            
        