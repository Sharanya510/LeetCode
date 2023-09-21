class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # BRUTE-FORCE
        # count = 0
        # n = len(grid)
        # for r in range(n):
        #     for c in range(n):
        #         match = True
        #         for i in range(n):
        #             if grid[r][i] != grid[i][c]:
        #                 match = False
        #                 break
        #         count += int(match)
        # return count
        
        count = 0
        n = len(grid)
        row_counter = collections.Counter(tuple(row) for row in grid)
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]
        return count
        
        
#         rows = len(grid)
#         cols = len(grid[0])
#         res = []
#         for i in range(rows):
#             temp = []
#             for j in range(cols):
#                 temp.append(grid[j][i])
#             res.append(temp)
#         # print(res)
#         count1 = 0
#         for r in res:
#             if r in grid:
               
#                 count1 += 1
#         count2 = 0
#         for rr in grid:
#             if rr in res:
#                 count2 += 1
#         return max(count1, count2)
        