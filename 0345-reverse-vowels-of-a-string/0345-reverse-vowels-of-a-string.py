class Solution:
    def reverseVowels(self, s: str) -> str:
        char_list = list(s)
        start = 0
        end = len(char_list) - 1
        while start < end:
            if self.isvowel(char_list[start]) and self.isvowel(char_list[end]) :
                char_list[start], char_list[end] = char_list[end], char_list[start]
                start += 1
                end -= 1
            elif not self.isvowel(char_list[start])  and self.isvowel(char_list[end]):
                start += 1
            elif self.isvowel(char_list[start])  and not self.isvowel(char_list[end]):
                end -= 1
            elif not self.isvowel(char_list[start])  and not self.isvowel(char_list[end]):
                start += 1
                end -= 1
        return "".join(char_list)
    
    def isvowel(self, c):
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            return True
        else:
            return False
        