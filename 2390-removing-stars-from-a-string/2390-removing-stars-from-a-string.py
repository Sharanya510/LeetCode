class Solution:
    def removeStars(self, s: str) -> str:
        my_stack = []
        for c in s:
            if c != '*':
                my_stack.append(c)
            elif c == '*':
                my_stack.pop()
        return ''.join(my_stack)
        