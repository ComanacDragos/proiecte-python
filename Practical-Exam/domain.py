from texttable import Texttable
import random
import copy
class Board:
    def __init__(self):
        self._board = []
        for i in range(9):
            line = []
            for j in range(9):
                line.append(-1)
            self._board.append(line)
        s = "ABCDEFGH"
        for i in range(9):
            self._board[0][i] = i
        for i in range(8):
            self._board[i+1][0] = s[i]


        self.bligons = 3
        self.ship = []
        self.place_stars()
        self.place_ship()
        self.place_bligons(3)


    def place_ship(self):
        while True:
            row = random.choice(range(1,9))
            col = random.choice(range(1,9))
            if self._board[row][col] == -1:
                self._board[row][col] = 9
                self.ship = [row,col]
                return

    def delete_bligons(self):
        for i in range(1,9):
            for j in range(1,9):
                if self._board[i][j] == 11:
                    self._board[i][j] = -1

    def place_bligons(self,nr):
        self.delete_bligons()
        b = nr
        while b>0:
            row = random.choice(list(range(1, 9)))
            col = random.choice(list(range(1, 9)))
            if self._board[row][col] == -1:
                b-=1
                self._board[row][col] = 11

    def neighbors(self, i, j):
        '''
        Returns all neighbors for a given posititon
        :param i: row
        :param j: column
        :return: list of neighbors
        '''
        neighbors = []
        if i > 1 and i < 8 and j > 1 and j < 8:
            neighbors.append([i+1,j])
            neighbors.append([i+1, j+1])
            neighbors.append([i+1, j-1])
            neighbors.append([i-1, j-1])
            neighbors.append([i-1, j])
            neighbors.append([i-1, j+1])
            neighbors.append([i, j-1])
            neighbors.append([i, j+1])
            return neighbors
        if i == 1 and j > 1 and j < 8:
            neighbors.append([i, j+1])
            neighbors.append([i, j-1])
            neighbors.append([i+1, j])
            neighbors.append([i+1, j+1])
            neighbors.append([i+1, j-1])
            return neighbors

        if i == 8 and j > 1 and j < 8:
            neighbors.append([i, j+1])
            neighbors.append([i, j-1])
            neighbors.append([i-1, j+1])
            neighbors.append([i-1, j-1])
            neighbors.append([i-1, j])
            return neighbors
        if j == 1 and i > 1 and i <8:
            neighbors.append([i+1,j])
            neighbors.append([i-1, j])
            neighbors.append([i+1, j+1])
            neighbors.append([i-1, j+1])
            neighbors.append([i, j + 1])
            return neighbors

        if j == 8 and i > 1 and i <8:
            neighbors.append([i+1,j])
            neighbors.append([i-1, j])
            neighbors.append([i+1, j-1])
            neighbors.append([i-1, j-1])
            neighbors.append([i, j - 1])
            return neighbors

        if i == 1 and j == 1:
            neighbors.append([i+1,j])
            neighbors.append([i, j+1])
            neighbors.append([i+1, j+1])
            return neighbors

        if i == 1 and j == 8:
            neighbors.append([i+1, j])
            neighbors.append([i, j-1])
            neighbors.append([i+1, j-1])
            return neighbors

        if i == 8 and j == 1:
            neighbors.append([i-1, j])
            neighbors.append([i, j+1])
            neighbors.append([i-1,j+1])
            return neighbors

        if i == 8 and j ==8:
            neighbors.append([i, j-1])
            neighbors.append([i-1, j])
            neighbors.append([i-1, j-1])
            return neighbors

    def place_stars(self):
        '''
        Places 10 stars randomly
        :return:
        '''
        stars = 10
        while stars>0:
            row = random.choice(list(range(1,9)))
            col = random.choice(list(range(1,9)))
            neighbors = self.neighbors(row, col)
            ok = 1
            if self._board[row][col] != -1:
                ok = 0
            for i in neighbors:
                if self._board[i[0]][i[1]] == 10:
                    ok = 0

            if ok == 1:
                stars -= 1
                self._board[row][col] = 10
                #print(row,col, self.neighbors(row, col))


    def __getitem__(self, item):
        return self._board[item]


    def __str__(self):
        t = Texttable()
        symbols ={
             -1 : "",
            10 : "*",
            9 : "E",
            11: "B",
        }

        board = copy.deepcopy(self._board)
        for i in range(1,9):
            for j in range(1,9):
                if [i,j] not in self.neighbors(self.ship[0], self.ship[1]):
                    if board[i][j] == 11:
                        board[i][j] = -1


        t.add_row(board[0])
        for i in range(1,9):
            line = []
            line.append(board[i][0])
            for j in range(1,9):
                line.append(symbols[board[i][j]])
            t.add_row(line)
        return t.draw()

    def cheat(self):
        t = Texttable()
        symbols = {
            -1: "",
            10: "*",
            9: "E",
            11: "B",
        }
        t.add_row(self._board[0])
        for i in range(1, 9):
            line = []
            line.append(self._board[i][0])
            for j in range(1, 9):
                line.append(symbols[self._board[i][j]])
            t.add_row(line)
        return t.draw()

    def warp(self, coord):

        s = ["A", "B", "C", "D", "E", "F", "G", "H"]
        if coord[0] not in s:
            raise BadMove("Bad move")
        if len(coord) != 2:
            raise BadMove("Bad move")

        if int(coord[1]) not in list(range(1,9)):
            raise BadMove("Bad move")

        row = 1
        col = int(coord[1])
        for i in s:
            if coord[0] == i:
                break
            row += 1
        self.same(row, col)
        self.star_in_way(row,col)
        if self._board[row][col] == 11:
            raise GameOver("game over")
        if self._board[row][col] != -1:
            raise BadMove("Bad move")

        self._board[self.ship[0]][self.ship[1]] = -1
        self.ship[0] = row
        self.ship[1] = col
        self._board[row][col] = 9

    def star_in_way(self, x,y):
        if x<self.ship[0]:
            row1 = x
            row2 = self.ship[0]
        else:
            row1 = self.ship[0]
            row2 = x

        if y<self.ship[1]:
            col1 = y
            col2 = self.ship[1]
        else:
            col1 = self.ship[1]
            col2 = y

        if col1 == col2:
            for i in range(row1, row2+1):
                if self._board[i][col1] == 10:
                    raise BadMove("bad move")
        if row1 == row2:
            for j in range(col1,col2+1):
                if self._board[row1][j] == 10:
                    raise BadMove("Bad move")

        if col1 < col2:
            for i in range(row2-row1):
                if self._board[row1-i][col1-i] == 10:
                    raise  BadMove("Bad move")


        if col1 > col2:
            for i in range(row2-row1):
                if self._board[row1+i][col1+i]:
                    raise  BadMove("Bad move")



    def fire(self, coord):
        s = ["A", "B", "C", "D", "E", "F", "G", "H"]
        if coord[0] not in s:
            raise BadMove("Bad move")
        if len(coord) != 2:
            raise BadMove("Bad move")

        if int(coord[1]) not in list(range(1, 9)):
            raise BadMove("Bad move")

        row = 1
        col = int(coord[1])
        for i in s:
            if coord[0] == i:
                break
            row += 1

        neighbours = self.neighbors(self.ship[0], self.ship[1])
        if [row,col] not in neighbours:
            raise BadMove("Bad fire")

        if self._board[row][col] != 11:
            raise BadMove("Bad fire")

        for i in neighbours:
            if self._board[i[0]][i[1]] == 11:
                self._board[i[0]][i[1]] = -1
                self.bligons -= 1

                if self.bligons == 0:
                    raise Won("Game won")
                self.place_bligons(self.bligons)



    def same(self,x,y):
        row = self.ship[0]
        col = self.ship[1]
        if row == x or col == y:
            return
        #if col !=y:
         #   raise BadMove("Bad Move")

        ok = 0
        for i in range(1,9):

            if x+i == row and y+i == col:
                ok = 1

            if x + i == row and y - i == col:
                ok = 1

            if  x-i == row  and y-i ==col:
                ok = 1
            if x - i == row and y + i == col:
                ok = 1

        if ok == 0:
            raise BadMove("Bad move")

class GameOver(Exception):
    pass
class StarInTheWay(Exception):
    pass
class BadMove(Exception):
    pass
class GameOver(Exception):
    pass
class Won(Exception):
    pass