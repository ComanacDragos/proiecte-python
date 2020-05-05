import unittest
from domain import *

class MyTestCase(unittest.TestCase):
    def test_neighbors(self):
        board = Board()
        l1 = board.neighbors(1,1)
        l2 = board.neighbors(2,2)
        l3 = board.neighbors(8,7)
        test_l1 = [[2, 1], [1, 2], [2,2]]
        test_l2 = [[3, 2], [3, 3], [3, 1], [1, 1], [1, 2], [1, 3], [2, 1], [2, 3]]
        self.assertEqual(l1,test_l1)
        self.assertEqual(l2, test_l2)
        self.assertEqual(l3,[[8, 8], [8, 6], [7, 8], [7, 6], [7, 7]])


    def test_place_stars(self):

        for j in range(100):
            cont = 0
            board = Board()
            for i in range(1,9):
                for j in range(1,9):
                    if board[i][j] == 10:
                        cont += 1
                        ok = 1
                        for k in board.neighbors(i,j):
                            if board[k[0]][k[1]] == 10:
                                ok = 0
                                print(board)
                                break
                        self.assertEqual(ok, 1)
        self.assertEqual(cont,10)



if __name__ == '__main__':
    unittest.main()
