# from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [-1] * n
        right = [-1] * n
        prefix = [0]
        
        # Update left array
        last_pipe_position = -1
        for i in range(n):
            if s[i] == '|':
                last_pipe_position = i
            left[i] = last_pipe_position
        
        # Update right array
        last_pipe_position = n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last_pipe_position = i
            right[i] = last_pipe_position
        
        # Update prefix array
        for i in range(n):
            if s[i] == '*':
                prefix.append(1 + prefix[-1])
            else:
                prefix.append(prefix[-1])
        
        ans = []
        
        for l, r in queries:
            r = left[r]
            l = right[l]
            if l > r:
                ans.append(0)
            else:
                ans.append(prefix[r + 1] - prefix[l])
        
        return ans

            
        
        
        
        # BRUTE FORCE -- MY SOLUTION
#         res = [0]*len(queries)
#         for index, query in enumerate(queries):
#             res[index] = self.helper(query, s)
#         return res
            
#     def helper(self, query, s):
#         substring = s[query[0] : query[1]+1]
#         left = 0
#         right = len(substring) - 1
#         count = 0
#         while left < right:
#             if substring[left] == substring[right] == '|':
#                 for i in range(left, right ):
#                     if substring[i] == '*':
#                         count += 1
#                 break
#             elif substring[left] == '|' and substring[right] =='*':
#                 right -= 1
#             elif substring[left] == '*' and substring[right] =='|':
#                 left += 1
#             else:
#                 left += 1
#                 right -= 1
#         return count
                
            
        