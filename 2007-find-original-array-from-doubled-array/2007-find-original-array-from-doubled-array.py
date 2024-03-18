class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        my_hashmap = Counter(changed)    
        original = []
        for num in changed:
            if my_hashmap[num] > 0 :
                my_hashmap[num] -= 1
                twiceNum = num * 2
                if twiceNum in my_hashmap and my_hashmap[twiceNum] > 0:
                    my_hashmap[twiceNum] -= 1
                    original.append(num)
                else:
                    return []
        return original