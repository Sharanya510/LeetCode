class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        p1, p2 = 0, 0
        while p1 < s_length and p2 < t_length and p2 >= 0 :
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            elif s[p1] != t[p2]:
                p2 += 1
        return p1 == len(s)