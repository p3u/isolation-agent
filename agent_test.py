"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

def time_left():
    return 1000

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer(search_depth=2)
        self.player2 = game_agent.AlphaBetaPlayer(search_depth=2)
        self.game = isolation.Board(self.player1, self.player2, width=9, height=9)
        self.game.apply_move((4, 4))
        self.game.apply_move((5, 4))

        self.game.apply_move((2, 5))
        self.game.apply_move((2, 1))

        self.game.apply_move((4, 2))
        self.game.apply_move((5, 2))

        self.game.apply_move((3, 4))
        self.game.apply_move((6, 4))

        self.game.apply_move((4, 5))
        self.game.apply_move((5, 5))

        self.game.apply_move((4, 5))
        self.game.apply_move((5, 5))

        self.game.apply_move((4, 6))
        self.game.apply_move((3, 7))

        self.game.apply_move((2, 4))
        self.game.apply_move((4, 3))


        print(self.game.to_string())


    def test_minimax(self):
        self.player2.get_move(self.game, time_left)


if __name__ == '__main__':
    unittest.main()
