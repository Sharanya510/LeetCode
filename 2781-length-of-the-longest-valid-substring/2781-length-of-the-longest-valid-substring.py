class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        rst = 0
        l = 0
        for i in range(len(word)):
            for j in range(max(l, i-10), i+1):
                if word[j:i+1] in s:
                    l = j+1
            rst = max(rst, i-l+1)
        return rst