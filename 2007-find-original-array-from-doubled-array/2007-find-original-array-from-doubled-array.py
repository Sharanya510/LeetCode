class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c, res = Counter(changed), []
        changed.sort()
        for num in changed:
            double = 2 * num
            if double in c:
                if (num and c[num] >= 1) or (num == 0 and c[num] >= 1):
                    c[num] -= 1
                    c[double] -= 1
                    res.append(num)
        
        for num in c:
            if c[num] != 0:
                return []
        return res 