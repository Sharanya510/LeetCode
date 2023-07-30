class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.helper(s, 0, len(s)-1)
    
    def helper(self, s, left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            self.helper(s, left+1, right-1)
        
        