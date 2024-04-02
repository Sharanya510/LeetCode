class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = []    
        
        for c in s:                            
            if stck and stck[-1][0] == c: # check if stack is not empty
                stck[-1][1]+=1
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])            
        
        return ''.join(c * cnt for c, cnt in stck)
        
#         left = 0
#         right = left + 1
#         while right < len(s)-1:
#             if len(s) <= k:
#                 return s
            
#             if s[left] != s[right]:
#                 left += 1
#                 right = left+1
#             else:
#                 while (right - left + 1) != k:
#                     right += 1
                
#                 if (right - left + 1) == k and s[left] == s[right] :
#                     s = s[:left] + s[right+1:]
#                     left, right = 0, 1
#         return s

        # len(s[left:right+1])
    