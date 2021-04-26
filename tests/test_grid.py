"""Test grid.py"""
import unittest

from playful.grid import Grid
from playful.point import Point


class TestGrid(unittest.TestCase):
    """Test Grid class"""

    def test_create(self):
        """Test creating a small, 2x2 grid of points"""
        points = {Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)}
        expected = Grid(points)
        actual = Grid.create(width=2, height=2)
        self.assertEqual(actual, expected)
