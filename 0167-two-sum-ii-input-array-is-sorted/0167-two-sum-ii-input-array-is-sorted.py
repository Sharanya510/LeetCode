class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
        # my_hashmap = {}
        # for index, number in enumerate(numbers):
        #     diff = target - number
        #     if diff not in my_hashmap:
        #         my_hashmap[number] = index
        #     else:
        #         return [ index + 1, my_hashmap[diff] + 1]