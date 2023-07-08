class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        # strs.sort()
        res = []
        for i in range(len(strs)-1):
            temp = ""
            for j in range(min(len(strs[i]),len(strs[i+1]))):
                if strs[i][j]==strs[i+1][j]:
                    temp+=strs[i][j]
                else:
                    break
            res.append(temp)
        return min(res)
        