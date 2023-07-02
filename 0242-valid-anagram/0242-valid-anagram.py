class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        
        
        #TWO HASHMAPS
#         s_map, t_map = {}, {}
#         for c in s:
#             if c not in s_map:
#                 s_map[c] = 1
#             else:
#                 s_map[c] += 1
#         for c in t:
#             if c not in t_map:
#                 t_map[c] = 1
#             else:
#                 t_map[c] += 1
        
#         return s_map == t_map
        
        # BRUTE--FORCE
        # if len(s) != len(t):
        #     return False
        # else:
        #     return sorted(s) == sorted(t)
        