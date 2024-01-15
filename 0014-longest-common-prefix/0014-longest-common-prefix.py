class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        prefix = strs[0]
        for i in range(len(prefix)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or prefix[i] != strs[j][i]:
                    return res
            res += prefix[i]
        return res
                