class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS = len(rooms)
        COLS = len(rooms[0])
        stack = []
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    stack.append((r,c))
        # print(stack)
        level = 1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        nextStack = []
        while stack:
            r, c = stack.pop()
            for x, y in directions:
                if r+x >= 0 and c+y >= 0 and r+x<ROWS and c+y<COLS and rooms[r+x][c+y] == 2147483647:
                    nextStack.append((r+x,c+y))
                    rooms[r+x][c+y] = level
            # print(rooms)
            if len(stack) == 0 and len(nextStack) != 0:
                stack = nextStack
                nextStack = []
                level += 1
