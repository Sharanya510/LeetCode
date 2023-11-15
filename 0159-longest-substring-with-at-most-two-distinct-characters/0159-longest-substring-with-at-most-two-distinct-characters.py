class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = float("-inf")
        hash_map = defaultdict(list)
        counter = 0
        start = 0
        for end in range(len(s)):
            c = s[end]
            if c not in hash_map:
                hash_map[c] = 1
                counter += 1
            else:
                hash_map[c] += 1
                
            while counter > 2:
                left = s[start]
                hash_map[left] -= 1
                if hash_map[left] == 0:
                    del hash_map[left]
                    counter -= 1
                start +=1
            longest = max(longest, end - start + 1)
        return longest
        
                