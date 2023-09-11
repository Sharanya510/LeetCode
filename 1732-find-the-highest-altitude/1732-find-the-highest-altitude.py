class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_gain = 0
        highest_altitude = current_gain
        
        for i in gain:
            current_gain += i
            highest_altitude = max(highest_altitude, current_gain)
        return highest_altitude
        
        
        # res = [0]* (len(gain)+1)
        # for i in range(len(gain)):
        #     res[i+1] = res[i] + gain[i]
        # return max(res)
        
# -5  1   5   0   -7

