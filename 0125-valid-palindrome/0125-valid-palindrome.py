class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r :
            while l < r and not self.isalphanumer(s[l]):
                l += 1
            while l < r and not self.isalphanumer(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def isalphanumer(self, c):
        return (
        ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9"))
        
        
        
        # BRUTE--FORCE o(n)
#         res = ""
#         for c in s:
#             if c.isalnum():
#                 res += c
#             else:
#                 continue
#         # print(res)
#         rev_res = ""
#         for i in range(len(res)-1, -1, -1):
#             if res[i].isupper():
#                 rev_res += res[i].lower()
#             else:
#                 rev_res += res[i]
#         print(rev_res)
        
#         new_res = rev_res[::-1]
#         print(new_res)
#         return rev_res == new_res
                
                
                
                
            
            
        