class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, max_count = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        
        for i in range(k, len(s)):
            if s[i] not in vowels and s[i-k] in vowels:
                count -= 1
            elif s[i] in vowels and s[i-k] not in vowels :
                count += 1
                
            max_count = max(count, max_count)
            
        return max_count
    
    # a   b   c   i   i   i   d   e   f
    # count = 0
                
                
        