class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for c in s:
            if c == '(':
                my_stack.append(')')
            elif c == '[':
                my_stack.append(']')
            elif c == '{':
                my_stack.append('}')
            elif c == ')':
                if my_stack:
                    if my_stack[-1] == ')':
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
            elif c == ']':
                if my_stack:
                    if my_stack[-1] == ']':
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
            elif c == '}':
                if my_stack:
                    if my_stack[-1] == '}':
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(my_stack) == 0
        