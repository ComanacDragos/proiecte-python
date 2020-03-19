import random
import copy

class Word:
    def __init__(self, word):
        self.original = word
        self.score = 0
        #self.word = self.scramble()
        self.last_word = "abc"
        self.during_undo = 1
        self.scramble()


    def scramble(self):
        word = self.original
        word = word.split(" ")
        arr = []
        for i in word:
            l = []
            for j in i:
                l.append(j)
                self.score += 1
            arr.append(l)

        self.word = arr

        self.random_scramble()

    def random_scramble(self):
        score = self.score
        for i in range(len(self.word)):
            #print("tes")
            w1 = random.choice(range(len(self.word)))
            w2 = random.choice(range(len(self.word)))
            if len(self.word[w1]) <= 2 or len(self.word[w2]) <= 2:
                continue
            l1 = random.choice(range(1, len(self.word[w1]) - 1))
            l2 = random.choice(range(1, len(self.word[w2]) - 1))
            #print(w1, l1, w2, l2)
            try:
                self.swap(w1, l1, w2, l2)
            except GameWon:
                #self.score = score
                self.random_scramble()

            #if self.score == score:
              #  self.random_scramble()
        self.score = score

    def undo(self):
        if self.during_undo == 1:
            raise DuringUndo("No undo allowed")
        self.word = self.last_word[:]
        self.during_undo = 1

    def swap (self, w1, l1, w2, l2):

        if w1 >= len(self.word):
            raise BadCommand("Index of first word is bad")
        if l1 >= len(self.word[w1]):
            raise BadCommand("Index of first letter is bad")
        if w2 >= len(self.word):
            raise BadCommand("Index of second word is bad")
        if l2 >= len(self.word[w2]):
            raise BadCommand("Index of second letter is bad")

        #print(self.last_word)
        self.last_word = copy.deepcopy(self.word)
        self.during_undo = 0
        aux = self.word[w1][l1]
        self.word[w1][l1] = self.word[w2][l2]
        self.word[w2][l2] = aux
        self.score -= 1

        if self.score == 0:
            raise GameOver("You lost!")

        if self.original == self.__str__():
            raise GameWon("You win!")



    def __str__(self):
        word = ""
        for i in self.word:
            for j in i:
                word += j
            word += " "
        return word.strip()

    def __getitem__(self, item):
        return self.word[item]
"""
w = Word("dream without fear")
#w.swap(0,3,0,2)
print(w, w.score)"""

class GameWon (Exception):
    pass
class GameOver (Exception):
    pass
class BadCommand(Exception):
    pass
class DuringUndo (Exception):
    pass
