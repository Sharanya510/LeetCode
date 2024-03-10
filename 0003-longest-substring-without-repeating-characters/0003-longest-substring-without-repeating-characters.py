class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        counter = 0
        hash_map = defaultdict(int)
        for right in range(len(s)):
            right_char = s[right]
            hash_map[right_char] += 1
            if hash_map[right_char] > 1:
                counter += 1
                
                while counter > 0:
                    left_char = s[left]
                    if hash_map[left_char] > 1:
                        counter -= 1
                    hash_map[left_char] -= 1
                    left += 1
                    
                    
            max_length = max(max_length, right - left + 1)
        return max_length
                
                
# a   b   c   a   b   c   b   b
# l
# r
#     r
#         r
#             r
            