class Solution:
    def maxRepOpt1(self, text: str) -> int:
        charMap = defaultdict(list)

        l = 0
        for r in range(len(text)):
            if text[r] != text[l]:
                charMap[text[l]].append([l, r - l])
                l = r
        # print(charMap)
        charMap[text[-1]].append([l, r - l + 1])
        # print(charMap)
        # corner case: if there is only one element -> return length of the text
        if len(charMap) == 1:
            return len(text)

        res = 0
        for c, lst in charMap.items():
            prevStart, prevCount = lst[0]
            res = max(res, prevCount + (1 if len(lst) >= 2 else 0))
            if len(lst) >= 2:
                for curStart, curCount in lst[1:]:
                    # if can connect
                    one = len(lst) > 2
                    if prevStart + prevCount + 1 == curStart: # 0 + 1 + 1 == 2
                        res = max(res, prevCount + curCount + one)
                    else:
                        res = max(res, curCount + 1)

                    prevStart, prevCount = curStart, curCount
        return res 
