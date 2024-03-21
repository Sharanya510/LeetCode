class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                prev_temperature, prev_index = stack.pop()
                res[prev_index] = index - prev_index
            stack.append((temperature, index))
        return res
           
                