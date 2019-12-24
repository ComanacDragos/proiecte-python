from Obstruction.domain.board import *

class EasyAI:
    def __init__(self, board):
        self._board = board

    def generate_move (self):
        '''
        Returns the first free square of the board
        :return: the tupple (i,j) where i is the row of the free square and j is the column
        '''
        i = 0
        while i < self._board.rows:
            j = 0
            while j < self._board.columns:
                if self._board.valid_move(i, j):
                    return (i,j)
                j += 1
            i += 1

class BetterAI:
    def __init__(self, board):
        self._board = board

    def winning_move (self):
        pass