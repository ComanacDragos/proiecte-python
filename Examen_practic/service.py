from domain import *

class Service:
    def __init__(self, board):
        self._board = board

    def list_board(self):
        return str(self._board)

    def cheat(self):
        return self._board.cheat()

    def warp(self, coord):
        if len(coord) != 1:
            raise BadMove("Bad move")

        self._board.warp(coord[0])

    def fire(self, coord):
        if len(coord) != 1:
            raise BadMove("Bad fire")

        self._board.fire(coord[0])

