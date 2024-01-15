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
            max_length = max(max_length , right - left + 1)
        return max_length
            
            
        # APPROACH --> BRUTE FORCE
        # TIME COMPLEXITY --> O(N3)
        # SPACE COMPLEXITY --> O(N)
#         longest = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if self.check(i, j, s):
#                     longest = max(longest, j - i +1)
#         return longest
    
#     def check(self, start, end, s):
#         chars = set()
#         for i in range(start, end + 1):
#             if s[i] in chars:
#                 return False
#             chars.add(s[i])
#         return True