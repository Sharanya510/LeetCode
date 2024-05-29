class Solution:
    def scoreOfString(self, s: str) -> int:
        total_sum = 0
        for i in range(len(s) - 1):
            total_sum += abs(ord(s[i]) - ord(s[i+1]))
        return total_sum
    
    # h   e   l   l   o
    # 104 101 108 108 111
    # i = 0, 1, 2, 3
    # abs(s[0] - s[1])
            