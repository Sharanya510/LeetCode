class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        map_char = {}
        map_word = {}
        
        if len(words) != len(pattern):
            return False
        
        for char, word in zip(pattern, words):
            if char not in map_char:
                if word in map_word:
                    return False
                else:
                    map_char[char] = word
                    map_word[word] = char
            else:
                if map_char[char] != word:
                    return False
        return True
        
        