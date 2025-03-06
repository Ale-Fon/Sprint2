import unittest
from game_logic import gameplay

class TestSwitchTurn(unittest.TestCase):

    def setUp(self):
        self.game = gameplay(3)  # 3x3 Board

    def test_switch_turn(self):
        first_turn = self.game.current_turn
        self.game.switch_turn()
        self.assertNotEqual(self.game.current_turn, first_turn, "Turn should switch to the other player")
        self.game.switch_turn()
        self.assertEqual(self.game.current_turn, first_turn, "Turn should switch back to the initial player")

if __name__ == '__main__':
    unittest.main()