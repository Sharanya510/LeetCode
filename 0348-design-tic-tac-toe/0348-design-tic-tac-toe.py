class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
        # turn = 1 for player 1, -1 for player 2
        self.turn = 1


    def move(self, x: int, y: int, p: int) -> int:
        if p == 2:
            self.turn = -1
        # record result
        self.rows[x] += self.turn
        self.cols[y] += self.turn
        
        if x == y:
            self.diag += self.turn
            
        if x + y == self.n - 1:
            self.anti += self.turn
            
        # check result
        for line in (self.rows[x], self.cols[y], self.diag, self.anti):
            # print(line)
            if abs(line) == self.n:
                return p

        # we have no winner, so switch player
        self.turn = -self.turn
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)