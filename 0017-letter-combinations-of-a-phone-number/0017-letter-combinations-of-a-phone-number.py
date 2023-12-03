class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}
        
        def dfs(index, path):
            if len(path) == len(digits):
                combinations.append(path)
                return
            for char in letters[digits[index]]:
                dfs(index +1, path + char)
            
        combinations = []
        dfs(0, "")
        return combinations
        