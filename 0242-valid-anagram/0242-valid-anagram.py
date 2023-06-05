class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one line code
        # return sorted(s) == sorted(t)
        
        countS , countT = {}, {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)
        return countS == countT
        
        
        