from domain import *
import random
import copy

class Service:
    def __init__(self,board, AI= None):
        self.ai = AI
        self.board = board

    def get_board(self):
        return str(self.board)

    def save(self, filename):
        self.board.store_board(filename)

    @staticmethod
    def is_natural(n):
        try:
            n = float(n)
        except:
            raise ValueError
        else:
            if n < 0 or n != int(n):
                raise ValueError

    def human_move(self, row, col, symbol):
        try:
            self.is_natural(row)
        except:
            raise BadRowNumber("Row number is not a natural number")

        try:
            self.is_natural(col)

        except:
            raise BadColNumber("Col number is not a natural number")

        row = int(row)
        col = int(col)

        if row >=6:
            raise BadRowNumber("Row number is larger than 5")
        if col >=6:
            raise BadColNumber("Column number is larger than 5")

        if symbol not in ["X", "x", "O", "o"]:
            raise BadSymbol("Bad symbol")

        self.board.move(row, col, symbol)

    def computerMove (self):
        move = self.ai.generate_move()
        self.board.move(*move)


class AI:
    def __init__(self, board):
        self.board = board

    def generate_move(self):
        '''
        Generates a random valid move
        :return: the tupple (x,y)
        '''
        move = self.chaos_move()
        if move != None:
            return move

        l = []
        for i in range(6):
            for j in range(6):
                l.append([i,j])

        for i in range(6):
            for j in range(6):
                if self.board[i][j] != 0:
                    l.remove([i,j])
        move = random.choice(l)
        move.append("x")
        return move

    def chaos_move(self):
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == 0:
                    b1 = copy.deepcopy(self.board)
                    b2 = copy.deepcopy(self.board)
                    try:
                        move1 = [i,j,"x"]
                        b1.move(*move1)
                    except HumanWins:
                        return [i,j,"o"]
                    try:
                        move2 = [i,j,"o"]
                        b2.move(*move2)
                    except HumanWins:
                        return [i,j,"x"]