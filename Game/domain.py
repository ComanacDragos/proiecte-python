from texttable import Texttable

class Board:
    def __init__(self):
        self.data = []
        for i in range(6):
            line = [0] * 6
            self.data.append(line)
        self.lastMove = [-1,-1, 0]

    def __str__(self):
        t = Texttable()
        symbols = {
            0 : " ",
            1 : "O",
            -1 : "X"
        }

        for i in range(6):
            line = []
            for j in range(6):
                line.append(symbols[int(self.data[i][j])])
            t.add_row(line)
        return t.draw()

    def __getitem__(self, item):
        return self.data[item]

    def store_board(self, filename):
        f = open(filename, "w")
        for i in range(6):
            s = ''
            for j in range(6):
                s += str(self.data[i][j])
                s += " "
            s += '\n'
            f.write(s)
        f.close()

    def load_board (self, filename):
        f = open(filename, "r")
        self.data = []
        lines = f.readlines()
        for i in lines:
            i = i.strip().split(" ")
            line = []
            for j in i:
                line.append(int(j))
            self.data.append(line)
        f.close()

    def taken_square(self, row, col):
        if self.data[row][col] != 0:
            return True
        return False

    def move(self, row, col, symbol):
        symbols = {
            "x": -1,
            "X": -1,
            "O": 1,
            "o": 1
        }
        if self.data[row][col] != 0:
            raise BadMove("Square is taken")
        self.data[row][col] = symbols[symbol]
        self.lastMove = [row, col, symbol]
        self.player_win()
        self.computer_win()

    def computer_win (self):
        for i in self.data:
            for j in i:
                if j == 0:
                    return
        raise ComputerWins("Chaos has won")

    def check_row(self, n):
        s1 = 0
        s2 = 0
        for i in range(5):
            s1 += self.data[n][i]
            s2 += self.data[n][i+1]

        if abs(s1) == 5 or abs(s2) == 5:
            raise HumanWins("Order has won")

    def check_col(self, n):
        s1 = 0
        s2 = 0
        for i in range(5):
            s1 += self.data[i][n]
            s2 += self.data[i+1][n]

        if abs(s1) == 5 or abs(s2) == 5:
            raise HumanWins("Order has won")

    def check_diag(self):
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        for i in range(5):
            s1 += self.data[i][i]
            s2 += self.data[i+1][i+1]
            s3 += self.data[i+1][i]
            s4 += self.data[i][i+1]

        if abs(s1) == 5 or abs(s2) == 5 or abs(s3)==5 or abs(s4) ==5 :
            raise HumanWins("Order has won")

        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        for i in range(5):
            s1 += self.data[i][5-i]
            s2 += self.data[i+1][5-i]
            s3 += self.data[i][4-i]
            s4 += self.data[i+1][4-i]
        if abs(s1) == 5 or abs(s2) == 5:
            raise HumanWins("Order has won")

    def check_win(self):
        pass


    def player_win(self):
        for i in range(6):
            self.check_row(i)
            self.check_col(i)
        self.check_diag()



class BadMove(Exception):
    pass

class ComputerWins (Exception):
    pass

class HumanWins(Exception):
    pass

class BadSymbol(Exception):
    pass

class BadRowNumber(Exception):
    pass
class BadColNumber (Exception):
    pass
