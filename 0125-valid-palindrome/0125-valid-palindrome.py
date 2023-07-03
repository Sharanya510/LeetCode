class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r :
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        
        
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
                
                
                
                
            
            
        