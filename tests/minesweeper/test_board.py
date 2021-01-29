"""Test minesweeper/board.py"""
import unittest

from playful.point import Point
from playful.minesweeper.cell import Cell
from playful.minesweeper.board import Board


class TestPoint(unittest.TestCase):
    """Test Board class"""

    def test_bomb_count(self):
        """Test we correctly identify the number of bombs on a Board"""
        cells = {
            Cell(Point(0, 0), value=-1, state="hidden"),
            Cell(Point(1, 0), value=2, state="hidden"),
            Cell(Point(2, 0), value=-1, state="hidden"),
            Cell(Point(3, 0), value=2, state="hidden"),
            Cell(Point(4, 0), value=-1, state="hidden"),
        }
        self.assertEqual(Board(cells).bombs, 3)
