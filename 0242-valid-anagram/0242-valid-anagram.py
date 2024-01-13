class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t
        
        
        # APPROACH 2 HASHMAP ADDING AND COMPARING
        # TIME COMPLEXITY --> O(n)
        # SPACE COMPLEXITY --> O(n)
        # s_hashmap, t_hashmap = {}, {}
        # for char1 in s:
        #     if char1 not in s_hashmap:
        #         s_hashmap[char1] = 1
        #     else:
        #         s_hashmap[char1] += 1
        # for char2 in t:
        #     if char2 not in t_hashmap:
        #         t_hashmap[char2] = 1
        #     else:
        #         t_hashmap[char2] += 1
        # return s_hashmap == t_hashmap
        
        
# APPROACH 1 SORTING TWO WORDS
# TIME COMPLEXITY --> O(logn)
# SPACE COMPLEXITY --> O(1)
        # return sorted(s) == sorted(t)
        