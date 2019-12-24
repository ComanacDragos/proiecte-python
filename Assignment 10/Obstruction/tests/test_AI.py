import unittest
from Obstruction.controller.computerAI import *

class test_AI(unittest.TestCase):
    def test_generate_move(self):
        b = Board(3, 3)
        ai = EasyAI(b)

        b.move(0, 0, "X")
        self.assertEqual(ai.generate_move(), (0,2))
        b.move(0,2, "O")
        self.assertEqual(ai.generate_move(), (2,0))

if __name__ == '__main__':
    unittest.main()
