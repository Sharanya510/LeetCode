class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
        
# 30 --> 30 % 60 = 0
        
        # BRUTE FORCE -- TLE
        # count = 0
        # for i in range(len(time)):
        #     for j in range(i, len(time)):
        #         if i < j and (time[i] + time[j]) % 60 == 0:
        #             # print(time[i], time[j])
        #             count +=1
        # return count