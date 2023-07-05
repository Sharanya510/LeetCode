class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        length = 0
        i = 0
        max_length = 0
        for j in range(len(s)):
            if s[j] not in hash_map:
                hash_map[s[j]] = 1
                length = j - i + 1
                max_length = max(max_length, length)
            else:
                while s[j] in hash_map:
                    hash_map[s[i]] -= 1
                    if hash_map[s[i]] == 0:
                        del hash_map[s[i]]
                    i += 1
                hash_map[s[j]] = 1
                length = j - i + 1
                max_length = max(max_length, length)
        
        return max_length
            
        