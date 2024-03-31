class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total = 0
        mult = 1
        for i, c in enumerate(s):
            if c == "(":
                mult *= 2
            elif c == ")":
                if s[i - 1] == "(":
                    total += mult // 2 
                mult //= 2
        return total

