class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()
        
        
        
        # res = defaultdict(list)
        # for word in strs:
        #     count = [0]* 26
        #     for c in word:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(word)
        # return res.values()
                