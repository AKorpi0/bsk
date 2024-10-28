import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_creation(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at,0)

    def test_10_frame_game(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        f = Frame(2,6)
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(9))

    def test_11_frame_game(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        f = Frame(2,6)
        game.add_frame(f)
        self.assertRaises(BowlingError, game.add_frame, f)

    def test_score_of_1_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        self.assertEqual(6, game.calculate_score())

    def test_score_of_10_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        f = Frame(2,6)
        game.add_frame(f)
        self.assertEqual(81, game.calculate_score())


    def test_sparescore_of_2_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1,9))
        game.add_frame(Frame(8,1))
        self.assertEqual(27, game.calculate_score())

    def test_sparescore_of_10_frame(self):
        game = BowlingGame()
        game.add_frame(Frame(1,9))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        f = Frame(2,6)
        game.add_frame(f)
        self.assertEqual(88, game.calculate_score())