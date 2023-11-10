class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resul = 0
        length = len(digits)
        for i, n in enumerate(digits):
            resul += n * pow(10, length-i-1)
        resul = resul + 1
        # print(resul)
        res = [int(x) for x in str(resul)]
        return res