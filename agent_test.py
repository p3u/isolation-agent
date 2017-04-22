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
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2, width=5, height=5)
        self.game.apply_move((1, 2))
        self.game.apply_move((2, 3))

        self.game.apply_move((0, 0))
        self.game.apply_move((0, 2))

        self.game.apply_move((2, 1))
        self.game.apply_move((1, 0))

        self.game.apply_move((4, 0))

        print(self.game.to_string())


    def test_minimax(self):
        assert(self.player2.get_move(self.game, time_left) == (2, 2))

if __name__ == '__main__':
    unittest.main()
