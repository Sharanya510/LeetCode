class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap, t_hashmap = {}, {}
        for char1 in s:
            if char1 not in s_hashmap:
                s_hashmap[char1] = 1
            else:
                s_hashmap[char1] += 1
        for char2 in t:
            if char2 not in t_hashmap:
                t_hashmap[char2] = 1
            else:
                t_hashmap[char2] += 1
        return s_hashmap == t_hashmap
        
        
# APPROACH 1 SORTING TWO WORDS
# TIME COMPLEXITY --> O(logn)
# SPACE COMPLEXITY --> O(1)
        # return sorted(s) == sorted(t)
        