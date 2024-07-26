class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        ######################################################
        # TWO POINTER APPROACH
        ######################################################
        
        # Set of all characters of source. Can use a boolean array too.
        source_chars = set(source)

        # Check if all characters of target are present in source
        # If any character is not present, return -1
        for char in target:
            if char not in source_chars:
                return -1

        # Length of source to loop back to start of source using mod
        m = len(source)

        # Pointer for source
        source_iterator = 0

        # Number of times source is traversed. It will be incremented when
        # while finding the occurrence of a character in target, source_iterator
        # reaches the start of source again.
        count = 0

        # Find all characters of target in source
        for char in target:

            # If while finding, iterator reaches start of source again,
            # increment count
            if source_iterator == 0:
                count += 1

            # Find the first occurrence of char in source
            while source[source_iterator] != char:

                # Formula for incrementing while looping back to start.
                source_iterator = (source_iterator + 1) % m

                # If while finding, iterator reaches the start of source again,
                # increment count
                if source_iterator == 0:
                    count += 1

            # Loop will break when char is found in source. Thus, increment.
            # Don't increment count until it is not clear that target has
            # remaining characters.
            source_iterator = (source_iterator + 1) % m

        # Return count
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        ####################################################
        # BRUTE FORCE II -- CONCATENATE UNTIL SUBSEQUENCE
        ####################################################
#         # To check if to_check is subsequence of in_string
#         def is_subsequence(to_check, in_string):
#             i = j = 0
#             while i < len(to_check) and j < len(in_string):
#                 if to_check[i] == in_string[j]:
#                     i += 1
#                 j += 1

#             return i == len(to_check)

#         # Set of all characters of the source. We could use a boolean array as well.
#         source_chars = set(source)

#         # Check if all characters of the target are present in the source
#         # If any character is not present, return -1
#         for char in target:
#             if char not in source_chars:
#                 return -1

#         # Concatenate source until the target is a subsequence
#         # of the concatenated string
#         concatenated_source = source
#         count = 1
#         while not is_subsequence(target, concatenated_source):
#             concatenated_source += source
#             count += 1

#         # Number of concatenations done
#         return count