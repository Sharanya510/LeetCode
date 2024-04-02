class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        counts = []  # Stack to keep track of the counts of consecutive characters
        sa = list(s)  # Convert the string to a list for mutable operations
        j = 0  # Pointer for placing the next character in the 'compressed' version of the list

        for i in range(len(s)):
            sa[j] = sa[i]
            if j == 0 or sa[j] != sa[j - 1]:
                counts.append(1)
            else:
                incremented = counts.pop() + 1
                if incremented == k:
                    j -= k  # Remove k characters by moving j back k positions
                else:
                    counts.append(incremented)
            j += 1  # Increment j for the next unique character or sequence

        return ''.join(sa[:j])
        
        
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
        
    