"""Test minesweeper/cell.py"""
import unittest

from playful.point import Point
from playful.minesweeper.cell import Cell


class TestPoint(unittest.TestCase):
    """Test Cell class"""

    def test_neighbors(self):
        """Test returning a set of neighbors from a large group of Cells"""
        home = Cell(Point(4, 4), 2, "hidden")
        cells = {
            Cell(Point(4, 4), 2, "flagged"),
            Cell(Point(4, 5), 2, "hidden"),
            Cell(Point(3, 4), 2, "revealed"),
            Cell(Point(5, 5), 2, "revealed"),
            Cell(Point(3, 3), 2, "flagged"),
            Cell(Point(2, 3), 2, "hidden"),
            Cell(Point(4, 6), 2, "hidden"),
            Cell(Point(5, 6), 2, "hidden"),
        }
        neighbors = {
            Cell(Point(4, 5), 2, "hidden"),
            Cell(Point(3, 4), 2, "revealed"),
            Cell(Point(5, 5), 2, "revealed"),
            Cell(Point(3, 3), 2, "flagged"),
        }
        self.assertEqual(home.neighbors(cells), neighbors)

    def test_neighbor_states(self):
        """Test creating a dictionary of the states of neighboring Cells"""
        home = Cell(Point(4, 4), 2, "hidden")
        cells = {
            Cell(Point(4, 4), 2, "flagged"),
            Cell(Point(4, 5), 2, "hidden"),
            Cell(Point(3, 4), 2, "revealed"),
            Cell(Point(5, 5), 2, "revealed"),
            Cell(Point(3, 3), 2, "flagged"),
            Cell(Point(2, 3), 2, "hidden"),
            Cell(Point(4, 6), 2, "hidden"),
            Cell(Point(5, 6), 2, "hidden"),
        }
        neighbor_states = {"hidden": 1, "revealed": 2, "flagged": 1}
        self.assertEqual(home.neighbor_states(cells), neighbor_states)
