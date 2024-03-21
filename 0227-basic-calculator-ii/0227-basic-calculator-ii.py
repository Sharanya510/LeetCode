class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        current_number = 0
        operation = '+'
        for i, current_char in enumerate(s):
            if current_char.isdigit():
                current_number = (current_number * 10) + int(current_char)
            if not current_char.isdigit() and not current_char.isspace() or i == len(s) - 1:
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack_top = stack.pop()
                    stack.append(stack_top * current_number)
                elif operation == '/':
                    stack_top = stack.pop()
                    stack.append(int(stack_top / current_number))
                operation = current_char
                current_number = 0
        
        result = 0
        while stack:
            result += stack.pop()
        return result
