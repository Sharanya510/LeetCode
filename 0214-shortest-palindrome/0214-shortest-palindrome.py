class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
        return r + s
    
# Reverse the original string and store it in a variable r
# Iterate through each index i in the reversed string r
# Check if the original string s starts with the suffix of t from index i to the end
#If a palindrome suffix is found, prepend the remaining characters in t to s to create the shortest palindrome
#If no palindrome suffix is found, the entire reversed string t must be added to the front of s to create the shortest palindrome