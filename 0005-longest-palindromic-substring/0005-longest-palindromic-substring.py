class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""
                
# b   a   b   a   d
# l
# r
#     r
#         r
#             r
        
        
        # longest = 0
        # left, right = 0, 0
        # while left <= right:
        #     substring = s[left: right+1]
        #     reverse_substring = substring[::-1]
        #     if substring == reverse_substring:
        #         longest = max(longest, len(substring))
        #     right += 1
        # return longest
        