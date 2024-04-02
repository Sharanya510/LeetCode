class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_list = list(s)  # Convert string to list for mutable operations
        counts = []  # Stack to keep track of counts of consecutive characters

        i = 0  # Start from the first character
        while i < len(char_list):
            if i == 0 or char_list[i] != char_list[i - 1]:
                counts.append(1)  # Push count of 1 for a new character sequence
            else:
                incremented = counts.pop() + 1  # Increment count for consecutive character
                if incremented == k:
                    # If count reaches k, delete the consecutive characters
                    del char_list[i - k + 1:i + 1]
                    i -= k  # Adjust the index after deletion
                else:
                    counts.append(incremented)  # Push the incremented count back onto the stack
            i += 1  # Move to the next character

        return ''.join(char_list)  #
        
        
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
        
    