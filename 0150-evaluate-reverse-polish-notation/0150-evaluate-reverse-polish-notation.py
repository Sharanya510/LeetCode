class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+",  "-", "/", "*"]
        for token in tokens:
            if token not in operators:
                num = int(token)
                stack.append(num)
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            if token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            if token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            if token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
        return stack[-1]
            
        