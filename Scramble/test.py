import unittest
from UI import *

class MyTestCase(unittest.TestCase):
    def test_Word(self):
        word = Word("test1")

        self.assertEqual(word[0][0], "t")
        """self.assertEqual(word[0][1], "e")
        self.assertEqual(word[0][2], "s")
        self.assertEqual(word[0][3], "t")"""
        self.assertEqual(word[0][4], "1")
        self.assertEqual(len(word[0]), 5)

        word.swap(0,0,0, 4)
        self.assertEqual(word[0][0], "1")
        """self.assertEqual(word[0][1], "t")
        self.assertEqual(word[0][2], "s")
        self.assertEqual(word[0][3], "t")
        """
        self.assertEqual(word[0][4], "t")
        self.assertEqual(len(word[0]), 5)


if __name__ == '__main__':
    unittest.main()
