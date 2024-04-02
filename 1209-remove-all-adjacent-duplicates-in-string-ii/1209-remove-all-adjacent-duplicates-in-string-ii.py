class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        my_stack = []
        for c in s:
            if len(my_stack) != 0 and my_stack[-1][0] == c:
                my_stack[-1][1] += 1
                if my_stack[-1][1] == k:
                    my_stack.pop()
            else:
                my_stack.append([c, 1])
        return ''.join( c*count for c, count in my_stack)