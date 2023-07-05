class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        length = 0
        i = 0
        
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1
            
            while j - i + 1 - max(hash_map.values()) > k:
                hash_map[s[i]] -= 1
                i += 1
            length = max(length , j - i + 1)
        return length
        
        