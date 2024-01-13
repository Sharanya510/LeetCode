class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # APPROACH 1 --> SORTING
        # TIME COMPLEXITY --> O(NM LOGM) 
        # N --> LENGTH OF THE ARRAY
        # M --> MAX SIZE OF THE WORD IN THE ARRAY
        # SPACE COMPLEXITY --> O(NM)
        # res = defaultdict(list)
        # for s in strs:
        #     res[tuple(sorted(s))].append(s)
        # return res.values()
        
        
        # APPROACH 2 --> COUNTER
        # TIME COMPLEXITY --> O(NM)
        # N --. LENGTH OF THE ARRAY
        # M --> MAX LENGTH OF A WORD IN THE ARRAY
        # SPACE COMPLEXITY --> O(NM)
        res = defaultdict(list)
        for word in strs:
            count = [0]* 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return res.values()
                