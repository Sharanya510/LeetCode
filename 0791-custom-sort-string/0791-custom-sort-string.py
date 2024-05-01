class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map={}
        for c in s:
            if c not in hash_map:
                hash_map[c]=1
            else:
                hash_map[c]+=1
        # print(hash_map)
        #maintain a list for res instead of string as string is o(n)
        res= []
        for i in range(len(order)):
            if order[i] in hash_map:
                res.append(order[i]*hash_map[order[i]])
                # print(res)
                del hash_map[order[i]]
        for key,value in hash_map.items():
            res.append(key*value)
            # print(res)
        return ''.join(res)