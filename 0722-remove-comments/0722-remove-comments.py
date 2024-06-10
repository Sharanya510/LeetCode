class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        ans = []
        for line in source:
            i = 0
            if in_block == False:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and in_block == False:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block == True:
                    in_block = False
                    i += 1
                elif in_block == False and line[i:i+2] == '//':
                    break
                elif in_block == False:
                    newline.append(line[i])
                i += 1
            if newline and in_block == False:
                ans.append("".join(newline))

        return ans