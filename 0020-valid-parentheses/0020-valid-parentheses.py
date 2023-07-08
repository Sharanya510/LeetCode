class Solution:
    def isValid(self, s: str) -> bool:
        # for i in range(len(s)):
        #     if s[i] == '(' or '[' or '{':
        my_stack = []
        for c in s:
            if c == '{' :
                my_stack.append('}')
            elif c == '[':
                my_stack.append(']')
            elif c == '(':
                my_stack.append(')')
            elif c == ')':
                if my_stack:
                    if my_stack[-1] != ')':
                        return False
                    else:
                        my_stack.pop()
                else:
                    return False
            elif c == ']':
                if my_stack:
                    if my_stack[-1] != ']':
                        return False
                    else:
                        my_stack.pop()
                else:
                    return False
            elif c == '}':
                if my_stack:
                    if my_stack[-1] != '}':
                        return False
                    else:
                        my_stack.pop()
                else:
                    return False
        return len(my_stack) == 0
             
        
        
        
            
            
        