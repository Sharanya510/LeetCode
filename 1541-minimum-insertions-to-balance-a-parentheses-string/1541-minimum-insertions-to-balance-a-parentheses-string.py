class Solution:
    def minInsertions(self, s: str) -> int:
        # Initialize counters for the number of insertions required and the balance of open parentheses
        insertions, balance = 0, 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                # Increase balance for each open parenthesis
                balance += 1
            else:  # s[i] == ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    # If there's a consecutive closing parenthesis, match it with an open parenthesis if available
                    if balance > 0:
                        balance -= 1
                    else:
                        # If no open parenthesis is available, an insertion is needed
                        insertions += 1
                    i += 1  # Skip the next character since it's paired with the current one
                else:
                    # If there's no consecutive closing parenthesis, we need an extra insertion for balancing
                    if balance > 0:
                        balance -= 1
                    else:
                        insertions += 1
                    insertions += 1  # Additional insertion for the missing ')'
            i += 1
        # Each unbalanced '(' requires two ')' to balance out
        insertions += balance * 2
        return insertions
#         to_balance = 0
#         open_count, close_count = 0, 0
#         for c in s:
#             if c == '(':
#                 open_count += 1
#             elif open_count > 0 and c == ')':
#                 close_count += 1
#             elif open_count == 0 and c == ')':
#                 close_count += 1
#                 if close_count % 2 == 0:
#                     to_balance += close_count // 2
#                     close_count -= 2 * to_balance
#         return (2 * open_count - close_count + to_balance)
                

# (   )   (   )   )   )   )   (   ) 
# o=1
#     c= 1
#         o=2
#             c=2
#                 c=3
#                     c=4
#                         c=5
#                             o=3
#                                 c=6
        

# )   )   )   )   )   )   )    

# )   )   (   )   )   (   
# 1
#     2
#         0
#             -1
#                 -2
#                     0

# (   )   )
# 2
#     1
#         0
                
                
                
# (   (   )   )   )
# 2
#     4
#         3
#             2
#                 1