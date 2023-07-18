class Solution:
    def isValid(self, s: str) -> bool:
        stack_map = {'(': ')', '[': ']', '{': '}' }
        my_stack = []
        
        for c in s:
            if c in stack_map:
                my_stack.append(stack_map[c])
            elif my_stack:
                if my_stack[-1] == c :
                    my_stack.pop()
                else:
                    return False
            else:
                return False
        return len(my_stack) == 0
        
        
        
        
        
        
        # BRUTE--FORCE
#         my_stack = []
#         for c in s:
#             if c == '(':
#                 my_stack.append(')')
#             elif c == '[':
#                 my_stack.append(']')
#             elif c == '{':
#                 my_stack.append('}')
#             elif c == ')':
#                 if my_stack:
#                     if my_stack[-1] == ')':
#                         my_stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
#             elif c == ']':
#                 if my_stack:
#                     if my_stack[-1] == ']':
#                         my_stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
#             elif c == '}':
#                 if my_stack:
#                     if my_stack[-1] == '}':
#                         my_stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
                
#         return len(my_stack) == 0
        