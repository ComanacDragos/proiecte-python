import unittest
from service import *

class MyTestCase(unittest.TestCase):
    def test_AI(self):
        board = Board()
        ai = AI(board)
        l = [0,1,2,3,4,5]
        for i in range(1000):
            move = ai.generate_move()
            if move[0] in range(6) and move[1] in range(6):
                assert True
            else:
                assert False

        """l = []
        for i in range(6):
            for j in range(6):
                l.append([i, j])

        l.remove([1,3])
        for i in l:
            board.move(i[0], i[1], "x")

        self.assertEqual(ai.generate_move(), [1,3,"x"])
"""
    def test_chaosMove(self):
        board = Board()
        ai = AI(board)
        self.assertEqual(ai.chaos_move(), None)
        for i in range(4):
            board.move(1,i,"x")
        self.assertEqual(ai.chaos_move(), [1,4,"o"])

if __name__ == '__main__':
    unittest.main()
