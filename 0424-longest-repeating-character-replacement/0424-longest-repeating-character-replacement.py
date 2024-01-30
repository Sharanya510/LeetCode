class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # APPROACH --> SLIDING WINDOW
        # TIME COMPLEXITY --> O(N*M)
        # SPACE COMPLEXITY --> O(M), M = 26
        longest = 0
        hash_map = {}
        left = 0
        for right in range(len(s)):
            if s[right] in hash_map:
                hash_map[s[right]] += 1
            else:
                hash_map[s[right]] = 1
            
            while right - left + 1 - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
 
# 0   1   2   3
# A   B   A   B
# L
#             R -- A: 2, B: 3
#             RIGHT - LEFT + 1 --> 3 - 0 + 1 == 4
            
# A, AB, ABA, ABAB

# case 1 - replacing with A
# A   B   A   B   C ; K = 2
# A   A   A   B   C ; K = 1
# A   A   A   A   C; K = 0
# A   A   A   A   C ;

# case 2 - replacing with B
# A   B   A   B   C; K = 2
# B   B   A   B   C; K = 1
# B   B   B   B   C; K = 0
# B   B   B   B   C;

# case 3 - replacing with C
# A   B   C  C   C

# A   A   B   A   B   B   A

# A   A   A   A   B   B   A --> 4

# A   A   B   B   B   B   A --> 4


            