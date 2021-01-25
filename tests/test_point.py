"""Test point.py"""
import unittest

from playful.point import Point


class TestPoint(unittest.TestCase):
    """Test Point class"""

    def test_corners(self):
        """Test a point's corners"""
        point = Point(4, 4)
        corners = {Point(5, 5), Point(3, 5), Point(3, 3), Point(5, 3)}
        self.assertEqual(point.corners(), corners)

    def test_sides(self):
        """Test a point's sides"""
        point = Point(4, 4)
        sides = {Point(5, 4), Point(4, 5), Point(3, 4), Point(4, 3)}
        self.assertEqual(point.sides(), sides)
