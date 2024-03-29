class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        length = len(columnTitle)-1
        for i in range(len(columnTitle)-1, -1, -1):
            temp1 = ord(columnTitle[i]) - ord('A')
            temp2 = temp1 + 1
            res += temp2 * pow(26, (length-i))
        return res
        
        # for i in range(len(columnTitle)-1, -1, -1):
        #     temp1 = ord(columnTitle[i])
        #     temp1 = temp1 - 65
        #     temp2 = temp1 + 1
        #     res += temp2 * pow(26, (length - i))
        # return res
            

        