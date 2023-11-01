class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            if self.helper(pattern, query):
                res.append(True)
            else:
                res.append(False)
        return res
            
    def helper(self, pattern, query):
        i = 0
        for index, char in enumerate(query):
            if i < len(pattern) and pattern[i] == query[index]:
                i += 1
            elif char.isupper():
                return False
        return i == len(pattern)