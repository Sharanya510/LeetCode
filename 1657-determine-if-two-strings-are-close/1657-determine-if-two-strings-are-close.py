from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
#         count1 = Counter(word1)
#         count2 = Counter(word2)
#         print(count1)
#         print(count2)
        
#         return count1.keys() == count2.keys() and sorted(count1.values()) == sorted(count2.values())
        
        
        
        
        word1_hashmap , word2_hashmap = {}, {}
        for c in word1:
            if c not in word1_hashmap:
                word1_hashmap[c] = 1
            else:
                word1_hashmap[c] += 1
        for c in word2:
            if c not in word2_hashmap:
                word2_hashmap[c] = 1
            else:
                word2_hashmap[c] += 1
        return word1_hashmap.keys() == word2_hashmap.keys() and sorted(word1_hashmap.values()) == sorted(word2_hashmap.values())
            
# a   b   b   b   z   c   f
# a = 1; b = 3; c = 1; f = 1; z = 1
# b   a   b   z   z   c   z
# a = 1; b = 2; z = 3; c = 1
# word1 has more letters

# c   a   b   b   b   a
# a = 2; b = 3; c = 1
# a   a   b   b   s   s
# a = 2; b = 2; s = 2