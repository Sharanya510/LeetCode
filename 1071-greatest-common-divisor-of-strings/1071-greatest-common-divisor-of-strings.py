class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str2
        elif len(str1) < len(str2):
            str1, str2 = str2, str1
        elif str1[:len(str2)] != str2:
            return ""
        return self.gcdOfStrings(str1[len(str2):], str2)
        