class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        if not t:
            return False
        i, j = 0, 0
        res = ""
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                res += t[i]
                j += 1
            i += 1
        return s == res
        