class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # Dictionary to store the length of the longest chain ending with the word
        dp = {}
        
        # Sorting the list in terms of the word length
        words.sort(key=len)
        
        longest_word_sequence_length = 1
        
        for word in words:
            present_length = 1
            # Find all possible predecessors for the current word by removing one letter at a time
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in dp:
                    previous_length = dp[predecessor]
                    present_length = max(present_length, previous_length + 1)
            dp[word] = present_length
            longest_word_sequence_length = max(longest_word_sequence_length, present_length)
        
        return longest_word_sequence_length
    
#         #################################################
#         # TOP DOWN APPROACH + MEMOIZATION
#         #################################################
#       def dfs(self, words, memo, current_word):
#         # If the word is encountered previously, return its value from the memo (memoization).
#         if current_word in memo:
#             return memo[current_word]
        
#         # This stores the maximum length of word sequence possible with the 'current_word' as the start
#         max_length = 1
        
#         # Creating all possible strings by removing one character at a time from the `current_word`
#         for i in range(len(current_word)):
#             new_word = current_word[:i] + current_word[i + 1:]
#             # If the new word formed is present in the list, do a dfs search with this new_word.
#             if new_word in words:
#                 current_length = 1 + self.dfs(words, memo, new_word)
#                 max_length = max(max_length, current_length)
        
#         memo[current_word] = max_length
#         return max_length
    
#     def longestStrChain(self, words: List[str]) -> int:
#         memo = {}
#         words_present = set(words)
#         ans = 0
#         for word in words:
#             ans = max(ans, self.dfs(words_present, memo, word))
#         return ans