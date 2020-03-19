from domain import *
class Service:
    def __init__(self):
        f = open("input.txt", "r")
        lines = f.readlines()
        self.word = Word(random.choice(lines).strip())

    def get_word(self):
        return str(self.word) + " [The score is: " + str(self.word.score) + "]"

    @staticmethod
    def is_natural(n):
        try:
            n = float(n)
        except:
            raise ValueError
        else:
            if n < 0 or int(n) != n:
                raise ValueError

    def swap (self, params):
        if len(params) != 5:
            raise BadCommand("Bad number of parameters")
        if params[2] != "-":
            raise BadCommand("Bad command(need dash)")

        try:
            self.is_natural(params[0])
        except ValueError:
            raise BadCommand("Index of first word is bad")

        try:
            self.is_natural(params[1])
        except ValueError:
            raise BadCommand("Index of first letter is bad")

        try:
            self.is_natural(params[3])
        except ValueError:
            raise BadCommand("Index of second word is bad")

        try:
            self.is_natural(params[4])
        except ValueError:
            raise BadCommand("Index of second letter is bad")

        w1 = int(params[0])
        l1 = int(params[1])
        w2 = int(params[3])
        l2 = int(params[4])
        self.word.swap(w1,l1,w2,l2)

    def undo (self, params):
        if len(params) != 0:
            raise BadCommand("Bad number of parameters")

        self.word.undo()
