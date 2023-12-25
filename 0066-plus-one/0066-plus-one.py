class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        length = len(digits)
        for i, n in enumerate(digits):
            result += n * pow(10, length - i - 1)
        result = result +1
        new_res = [int(x) for x in str(result)]
        return new_res