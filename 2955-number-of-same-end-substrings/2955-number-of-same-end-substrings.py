class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(s)
        prefix_cnt = [[0] * 26 for _ in range(n)]
        for i in range(n):
            if i > 0:
                prefix_cnt[i] = prefix_cnt[i - 1][:]
            prefix_cnt[i][ord(s[i]) - ord('a')] += 1
        for l, r in queries:
            res = 0
            for i in range(26):
                if l > 0:
                    freq = prefix_cnt[r][i] - prefix_cnt[l - 1][i]
                else:
                    freq = prefix_cnt[r][i]
                res += freq + (freq * (freq - 1) // 2)
            ans.append(res)
        return ans