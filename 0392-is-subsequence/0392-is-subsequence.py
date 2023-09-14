class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ""
        # t_set = set(t)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res += s[i]
                i += 1
                j += 1
            else:
                j += 1
        return s == res
                