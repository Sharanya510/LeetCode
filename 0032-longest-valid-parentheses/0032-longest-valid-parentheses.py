class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        stack.append(-1)  # Initialize stack with a dummy value
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  
            else:
                stack.pop() 
                if len(stack) == 0:
                    stack.append(i)  
                else:
                    max_length = max(max_length, i - stack[-1])  
                
        return max_length
    
#     )   (   )   (   )   )
# [-1]
# []
#     [0]
#         [0, 1]
#             [0] maxlen = 2
#                  [0, 3]
#                     [0] max_len = 4
#                          [5]