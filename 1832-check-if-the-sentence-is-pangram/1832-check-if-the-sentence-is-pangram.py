from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return len(seen) == 26
    
        # METHOD -1
        # for i in range(26):
        #     curr_char = chr(ord('a') + i)
        #     if sentence.find(curr_char) == -1:
        #         return False
        # return True
    
        # count = Counter(sentence)
        # return len(count) == 26