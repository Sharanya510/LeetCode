from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = Counter(sentence)
        return len(count) == 26