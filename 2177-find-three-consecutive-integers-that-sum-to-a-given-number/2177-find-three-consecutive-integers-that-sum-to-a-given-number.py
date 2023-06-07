class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        avg = num // 3
        if (avg - 1) + avg + (avg + 1) == num:
            return [avg - 1, avg, avg +1]
        else:
            return []
        