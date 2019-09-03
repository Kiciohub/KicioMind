import unittest
from src import GameProcess


def mock_player_input_incorrect():
    return "50,50,50,50"


def mock_player_input_correct():
    return "10,20,30,40"


class AcceptanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.testgame = GameProcess.Game(4, 10, 10)
        self.testgame.sequence = [10, 20, 30, 40]

    def test_create_sequence(self):
        self.assertEqual(len(self.testgame.create_sequence(4, 10)), 4)
        self.assertLessEqual(max(self.testgame.create_sequence(4, 10)), 10)

    def test_sequence_check_exact_match(self):
        self.assertEqual(self.testgame.sequence_check([10, 20, 30, 40], [10, 20, 30, 40]), (4, 0))
        self.assertEqual(self.testgame.sequence_check([10, 10, 10, 10], [20, 20, 20, 20]), (0, 0))

    def test_sequence_check_in_sequence(self):
        self.assertEqual(self.testgame.sequence_check([10, 20], [20, 10]), (0, 2))
        self.assertEqual(self.testgame.sequence_check([10, 20, 20], [10, 10, 10]), (1, 0))

    def test_sequence_check_match_and_in_sequence(self):
        self.assertEqual(self.testgame.sequence_check([20, 40, 30, 10], [10, 40, 20, 10]), (2, 1))

    def test_sequence_check_not_match(self):
        self.assertEqual(self.testgame.sequence_check([10, 10], [20, 20]), (0, 0))

    def test_actual_game_loose(self):
        self.assertEqual(self.testgame.single_player_input(mock_player_input_incorrect()), (0, 0))

    def test_actual_game_win(self):
        self.assertEqual(self.testgame.single_player_input(mock_player_input_correct()), (4, 0))

    def test_dupa(self):
        self.assertEqual(GameProcess.dupa(1, 2), 2)
        self.assertEqual(GameProcess.dupa(1, 3), 3)
