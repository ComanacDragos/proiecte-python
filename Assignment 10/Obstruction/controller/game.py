from Obstruction.domain.board import *
from Obstruction.controller.validator import *

class Controller:
    def __init__(self, board, player, computer):
        self._board = board
        self._validator = Validator()
        self._playerSymbol = player
        self._computerSymbol = computer

    def get_board (self):
        '''
        Returns the board
        :return: board - object of type Board
        '''
        return self._board

    def player_move (self, x, y):
        '''
        Checks if a move given by the player is valid or not and raises an exception in the latter case
        :param x: the row
        :param y: the column
        :return: None
        '''
        self._validator.natural_number(x)
        self._validator.natural_number(y)

        x = int(x)-1
        y = int(y)-1

        if x not in range(0, self._board.rows):
            raise BadMove("Bad row number")

        if y not in range(0, self._board.columns):
            raise BadMove("Bad column number")

        if self._board.square (x, y) != 0:
            raise BadMove("Given square is taken")

        if self._board.valid_move(x,y) == False:
            raise BadMove("One of the neighbours is taken")

        self._board.move(x, y, self._playerSymbol)

        if self._board.is_won() == True:
            raise GameOver("Game is won by the player")



