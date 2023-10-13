class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        res = [[ float('inf') for j in range(len(mat[0]))] for i in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    res[i][j] = 0
        visited = set()
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dirs in directions:
                new_x = dirs[0] + i
                new_y = dirs[1] + j
                if new_x >= 0 and new_x < len(mat) and new_y >= 0 and new_y < len(mat[0]) and (new_x, new_y) not in visited and mat[new_x][new_y] == 1 and res[new_x][new_y] > res[i][j] + 1 :
                    queue.append((new_x, new_y))
                    res[new_x][new_y] = res[i][j] + 1
        return res