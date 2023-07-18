class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        hash_set = set()
        
        for j in range(len(s)):
            if s[j] not in hash_set:
                hash_set.add(s[j])
            else:
                while i <= j and s[j] in hash_set :
                    hash_set.remove(s[i])
                    i += 1
                hash_set.add(s[j])
            longest = max(longest, j - i + 1)
        return longest
        