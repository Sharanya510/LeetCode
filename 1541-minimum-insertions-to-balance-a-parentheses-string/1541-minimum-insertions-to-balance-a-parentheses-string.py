class Solution:
    def minInsertions(self, s: str) -> int:
         # Replace every '))' with a placeholder '#'
        s = s.replace('))', '#')

        missing = 0  # Tracks the number of insertions needed
        required = 0  # Tracks the required number of ')' to balance '('

        # Iterate through each character in the modified string
        for c in s:
            if c == '(':
                # Each '(' increases the required ')' count by 2
                required += 2
            else:  # Handle ')' or '#'
                if c == ')':
                    # Single ')' found, increment missing
                    missing += 1
                # Adjust required count based on available ')'
                if required > 0:
                    required -= 2
                else:
                    # If no '(' to match, increase missing for balancing
                    missing += 1
        
        # Return total insertions needed: unpaired ')' + remaining required ')'
        return missing + required
