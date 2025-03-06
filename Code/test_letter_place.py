import unittest
from game_logic import gameplay

class TestLetterPlace(unittest.TestCase):

    def setUp(self):
        self.game = gameplay(3)  # 3x3 Board

    def test_letter_place(self):
        self.game.letterPlace(0, 0, 'S')
        self.assertEqual(self.game.board[0][0], 'S', "Letter 'S' should be placed at (0, 0)")
        self.assertEqual(len(self.game.moves), 1, "Move should be recorded in moves list")

if __name__ == '__main__':
    unittest.main()