class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        mapping = { ")": "(", "}": "{", "]": "["}
        
        for c in s:
            if c in mapping:
                if my_stack:
                    top = my_stack.pop() 
                else:
                    return False
                if mapping[c] != top:
                    return False
            else:
                my_stack.append(c)
        return not my_stack
        
        
        
        
        
        
        # my_stack = []
        # for c in s:
        #     if c == '{' :
        #         my_stack.append('}')
        #     elif c == '[':
        #         my_stack.append(']')
        #     elif c == '(':
        #         my_stack.append(')')
        #     elif c == ')':
        #         if my_stack:
        #             if my_stack[-1] != ')':
        #                 return False
        #             else:
        #                 my_stack.pop()
        #         else:
        #             return False
        #     elif c == ']':
        #         if my_stack:
        #             if my_stack[-1] != ']':
        #                 return False
        #             else:
        #                 my_stack.pop()
        #         else:
        #             return False
        #     elif c == '}':
        #         if my_stack:
        #             if my_stack[-1] != '}':
        #                 return False
        #             else:
        #                 my_stack.pop()
        #         else:
        #             return False
        # return len(my_stack) == 0
             
        
        
        
            
            
        