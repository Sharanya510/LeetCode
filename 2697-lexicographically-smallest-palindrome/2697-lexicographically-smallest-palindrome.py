class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
    
        while left <= right:
            if s[left] != s[right]:
                if ord(s[left]) > ord(s[right]):
                    s[left] = s[right]
                else:
                    s[right] = s[left]
            left += 1
            right -= 1
    
        return ''.join(s)
        