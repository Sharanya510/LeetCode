class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start=end=0
        s1_map=defaultdict(int)
        for c in s1:
            s1_map[c]+=1
        counter=len(s1_map)
        while end<len(s2):
            char=s2[end]
            if char in s1_map:
                s1_map[char]-=1
                if s1_map[char]==0:
                    counter-=1
            end+=1
            while counter==0:
                left_char=s2[start]
                if left_char in s1_map:
                    s1_map[left_char]+=1
                    if s1_map[left_char]>0:
                        counter+=1
                if end-start==len(s1):
                    return True
                start+=1
        return False
    
        