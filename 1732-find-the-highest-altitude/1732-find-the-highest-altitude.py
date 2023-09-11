class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # max_gain = 0
        # initial_gain = 0
        # for i in range(len(gain)-1):
        #     gain[i] = gain[i+1] - gain[i]
        res = [0]* (len(gain)+1)
        for i in range(len(gain)):
            res[i+1] = res[i] + gain[i]
        return max(res)