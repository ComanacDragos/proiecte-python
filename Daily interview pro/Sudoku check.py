"""
Hi, here's your problem today. This problem was recently asked by Facebook:

A Sudoku board is a 9x9 grid, where each row, column and each 3x3 subbox contains the number from 1-9.
 Here's an example of a Sudoku board.
 012 345 678
-------------
|534|678|912| 0
|672|195|348| 1
|198|342|567| 2
|------------
|859|761|423| 3
|426|853|791| 4
|713|924|856| 5
|------------
|961|537|284| 6
|287|419|635| 7
|345|286|179| 8
|------------

Given a 9x9 board, determine if it is a valid Sudoku board.
 The board may be partially filled, where an empty cell will be represented by the space character ' '.

Here's an example and some starting code:

"""

def validate_sudoku(board):
    # Fill this in.
    for i in range(9):
        row = dict()
        col = dict()
        square = dict()
        for j in range(9):
            nr_row = board[i][j]
            nr_col = board[j][i]

            square_line = 3 * (i % 3) + j // 3
            square_column = 3 * (i % 3) + j % 3

            nr_square = board[square_line][square_column]

            if nr_row != ' ':
                if nr_row in row.keys():
                    return False
                row[nr_row] = True
            if nr_col != ' ':
                if nr_col in col.keys():
                    return False
                col[nr_col] = True
            if nr_square != ' ':
                if nr_square in square.keys():
                    return False
                square[nr_square] = True
        return True

board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))
# True