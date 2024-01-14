class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s.strip()
        i, j = 0, len(s)-1
        while i<=j:
            while i<= j and not s[i].isalnum():
                i += 1
            while i<= j and not s[j].isalnum():
                j -= 1
            if i<= j and s[i].isnumeric() and s[j].isnumeric():
                if s[i] != s[j]:
                    return False
            if i<= j and s[i].lower() != s[j].lower():
                return False
            else:
                i+=1
                j -= 1
        return True