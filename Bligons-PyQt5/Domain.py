"""
Board
"""
from random import random


class Board:
    """
    Board
    Codes:
    0 - empty position
    1 - star
    11 - player
    -1 - bligons
    """
    def __init__(self, size):
        self._size = size
        self._empty = 0
        self._star = 1
        self._player = 11
        self._bligon = -1

        self._board = []
        for i in range(self._size):
            self._board.append([0]*self._size)

        self.place_symbol(self._star, [self._star], 10)
        self.bligons_positions = self.place_symbol(self._bligon, [self._bligon], 3)
        self._player_position = self.place_symbol(self._player, [self._star, self._bligon], 1)[0]
        self.player_orientation = (0, 1)
        self._bligons = 3

    def place_symbol(self, symbol, bad_symbols, number_symbols):
        """
        Places number_symbols symbol but not next to symbols in bad_symbols
        Returns a list of occupied positions
        """
        positions = list()
        while number_symbols:
            row = int(random() * 1000 % self._size)
            column = int(random() * 1000 % self._size)

            if self._board[row][column] == 0:
                ok = True
                for pair in self.get_neighbours(row, column):
                    if self._board[pair[0]][pair[1]] in bad_symbols:
                        ok = False
                        break
                if not ok:
                    continue

                number_symbols -= 1
                self._board[row][column] = symbol
                positions.append((row, column))
        return positions

    def move_player(self, row, column):
        """
        Moves the player by the specified values
        """
        if self.player_orientation != (row, column):
            self.player_orientation = (row, column)
            return

        new_row = self._player_position[0] + row
        new_column = self._player_position[1] + column

        if not self.valid_position(new_row, new_column):
            raise BadMove

        if self._board[new_row][new_column] == self._star:
            raise BadMove

        if self._board[new_row][new_column] == self._bligon:
            raise GameLost

        current_row = self._player_position[0]
        current_column = self._player_position[1]

        self._board[current_row][current_column] = self._empty
        self._board[new_row][new_column] = self._player
        self._player_position = (new_row, new_column)

    def fire(self):
        """
        Fires in the cell to which the player points to
        """
        row = self.player_orientation[0] + self._player_position[0]
        column = self.player_orientation[1] + self._player_position[1]

        if not self.valid_position(row, column):
            return

        if self._board[row][column] == self._bligon:
            for pos in self.bligons_positions:
                self._board[pos[0]][pos[1]] = self._empty
            self._bligons -= 1

            if self._bligons == 0:
                raise GameWon

            self.bligons_positions = self.place_symbol(self._bligon, [self._bligon, self._player], self._bligons)

            for pos in self.bligons_positions:
                self._board[pos[0]][pos[1]] = self._bligon

    def get_neighbours(self, row, column):
        """
        Returns a list of all neighbours of a given position as row column pairs
        """
        neighbours = list()
        neighbours.append((row-1, column-1))
        neighbours.append((row-1, column))
        neighbours.append((row-1, column+1))
        neighbours.append((row+1, column-1))
        neighbours.append((row+1, column))
        neighbours.append((row+1, column+1))
        neighbours.append((row, column-1))
        neighbours.append((row, column+1))

        to_be_removed = list()
        for pair in neighbours:
            if pair[0] < 0 or pair[1] < 0 or pair[0] >= self._size or pair[1] >= self._size:
                to_be_removed.append(pair)

        for pair in to_be_removed:
            neighbours.remove(pair)

        return neighbours

    def __getitem__(self, item):
        return self._board[item]

    def is_star(self, code):
        """
        Returns true if the given code represents a star
        """
        return code == self._star

    def is_empty(self, code):
        """
        Returns true if the given code represents an empty position
        """
        return code == self._empty

    def is_player(self, code):
        """
        Returns true if the given code represents the player
        """
        return code == self._player

    def is_bligon(self, code):
        """
        Returns true if the given code represents a bligon
        """
        return code == self._bligon

    def valid_position(self, row, column):
        """
        Returns true if the given position is valid, false otherwise
        """
        return 0 <= row < self._size and 0 <= column < self._size

    def get_player_orientation(self):
        """
        Returns the orientation of the player:
            (1, 0) - down
            (-1, 0) - up
            (0, 1) - right
            (0-1) - left
        """
        return self.player_orientation

    def get_player_position(self):
        """
        Returns the position of the player
        """
        return self._player_position


class GameLost(Exception):
    """
    Game lost exception
    """
    pass


class GameWon(Exception):
    """
    Game lost exception
    """
    pass


class BadMove(Exception):
    """
    Bad move exception
    """
    pass
