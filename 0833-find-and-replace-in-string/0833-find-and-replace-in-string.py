class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a list of operations as tuples
        operations = sorted(zip(indices, sources, targets), reverse=True)
        
        # Convert the string to a list for easier manipulation
        s = list(s)
        
        for index, source, target in operations:
            # Check if the substring at the given index matches the source
            if ''.join(s[index:index + len(source)]) == source:
                # Perform the replacement
                s[index:index + len(source)] = list(target)
        
        # Convert the list back to a string
        return ''.join(s)

