class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        hash_map = {}
        left = 0
        for right in range(len(s)):
            if s[right] in hash_map:
                hash_map[s[right]] += 1
            else:
                hash_map[s[right]] = 1
            
            while right - left + 1 - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
            