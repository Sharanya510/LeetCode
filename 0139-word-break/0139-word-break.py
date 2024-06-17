class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)] == True:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]
        
        
        # words = set(wordDict)
        # queue = deque([0])
        # seen = set()
        # while queue:
        #     start = queue.popleft()
        #     if start == len(s):
        #         return True
        #     for end in range(start + 1, len(s) + 1):
        #         if end in seen:
        #             continue
        #         if s[start:end] in words:
        #             queue.append(end)
        #             seen.add(end)
        # return False