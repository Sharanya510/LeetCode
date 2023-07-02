class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =defaultdict(list)
        res = []
        for word in strs:
            new_word = ''.join(sorted(word))
            # print(new_word)
            if new_word not in d:
                d[new_word] = [word]
            else:
                d[new_word].append(word)
        print(d)
        
        for key, value in d.items():
            res.append(value)
        return res
        