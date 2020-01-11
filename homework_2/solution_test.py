import unittest
import tic_tac_toe

from tic_tac_toe import TicTacToeBoard

class SolutionTest(unittest.TestCase):

    def test_can_move_when_cell_valid(self):
        board = TicTacToeBoard()
        board["B1"] = "X"
        board["C1"] = "O"
        self.assertEqual(board["B1"], "X")
        self.assertEqual(board["C1"], "O")

    def test_move_twice_with_same_value(self):
        board = TicTacToeBoard()
        with self.assertRaises(tic_tac_toe.NotYourTurn):
            board["A1"] = 'X'
            board["B1"] = 'X'

    def test_print_full_board(self):
        board = TicTacToeBoard()
        board_str = """
  -------------
3 | X | X | X |
  -------------
2 | O | O | X |
  -------------
1 | O | X | O |
  -------------
    A   B   C
"""
        board["A3"] = "X"
        board["A2"] = "O"
        board["B3"] = "X"
        board["B2"] = "O"
        board["C3"] = "X"
        board["C1"] = "O"
        board["C2"] = "X"
        board["A1"] = "O"
        board["B1"] = "X"
        self.assertEqual(board_str.strip(), str(board).strip())


if __name__ == "__main__":
    unittest.main()
