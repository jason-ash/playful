"""Test minesweeper/board.py"""
import unittest

from playful.point import Point
from playful.minesweeper.cell import Cell
from playful.minesweeper.board import Board


class TestPoint(unittest.TestCase):
    """Test Board class"""

    cells = {
        Cell(Point(0, 0), value=-1, state="hidden"),
        Cell(Point(1, 0), value=2, state="revealed"),
        Cell(Point(0, 1), value=-1, state="flagged"),
        Cell(Point(1, 1), value=2, state="revealed"),
    }

    def test_bomb_count(self):
        """Test correctly identifying the number of bombs on a Board"""
        self.assertEqual(Board(self.cells).bombs, 2)

    def test_height(self):
        """Test correctly identifying calculate the height of the Board"""
        self.assertEqual(Board(self.cells).height, 2)

    def test_width(self):
        """Test correctly identifying calculate the width of the Board"""
        self.assertEqual(Board(self.cells).width, 2)

    def test_states(self):
        """Test correctly identifying the states of the Board's Cells"""
        expected = dict(hidden=1, revealed=2, flagged=1)
        self.assertEqual(Board(self.cells).states(), expected)
