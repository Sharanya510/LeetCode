class Solution:
    def minInsertions(self, s: str) -> int:
        # Initialize counters for the number of insertions 
        # required and the balance of open parentheses
        insertions, balance = 0, 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                # Increase balance for each open parenthesis
                balance += 1
            else:  # s[i] == ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    # If there's a consecutive closing parenthesis, 
                    # match it with an open parenthesis if available
                    if balance > 0:
                        balance -= 1
                    else:
                        # If no open parenthesis is available, an insertion is needed
                        insertions += 1
                    i += 1  # Skip the next character since it's paired with the current one
                else:
                    # If there's no consecutive closing parenthesis, 
                    # we need an extra insertion for balancing
                    if balance > 0:
                        balance -= 1
                    else:
                        insertions += 1
                    insertions += 1  # Additional insertion for the missing ')'
            i += 1
        # Each unbalanced '(' requires two ')' to balance out
        insertions += balance * 2
        return insertions
