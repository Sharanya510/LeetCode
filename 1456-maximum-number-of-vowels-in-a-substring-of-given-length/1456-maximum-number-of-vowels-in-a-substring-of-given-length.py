class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count +=1 
            if s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count
        
#         length = 0
#         max_length = 0
#         i = 0
#         while i < len(s)-k+1:
#             sub_string = s[i : i+k]
#             length = self.vowelength(sub_string)
#             max_length = max(max_length, length)
#             i += 1 
#         return max_length
    
#     def vowelength(self, s):
#         length = 0
#         for char in s:
#             if char == 'a' or  char =='e' or  char =='i' or  char =='o' or  char =='u':
#                 length += 1
#         return length