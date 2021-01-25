"""Test point.py"""
import unittest

from playful.point import Point


class TestPoint(unittest.TestCase):
    """Test Point class"""

    def test_borders(self):
        """Test a Point's borders"""
        point = Point(4, 4)
        borders = {
            Point(5, 5),
            Point(3, 5),
            Point(3, 3),
            Point(5, 3),
            Point(5, 4),
            Point(4, 5),
            Point(3, 4),
            Point(4, 3),
        }
        self.assertEqual(point.borders(), borders)

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

    def test_is_border(self):
        """Test identifying whether two points border each other"""
        self.assertTrue(Point(4, 4).is_border(Point(5, 5)))
        self.assertTrue(Point(5, 5).is_border(Point(4, 4)))
        self.assertTrue(Point(4, 4).is_border(Point(4, 5)))
        self.assertTrue(Point(4, 5).is_border(Point(5, 5)))
        self.assertFalse(Point(4, 4).is_border(Point(6, 6)))

    def test_is_corner(self):
        """Test identifying whether two points are corners of each other"""
        self.assertTrue(Point(4, 4).is_corner(Point(5, 5)))
        self.assertTrue(Point(5, 5).is_corner(Point(4, 4)))
        self.assertFalse(Point(4, 4).is_corner(Point(4, 5)))
        self.assertFalse(Point(4, 5).is_corner(Point(4, 4)))

    def test_is_side(self):
        """Test identifying whether two points are sides of each other"""
        self.assertTrue(Point(4, 4).is_side(Point(4, 5)))
        self.assertTrue(Point(4, 5).is_side(Point(5, 5)))
        self.assertFalse(Point(4, 4).is_side(Point(5, 5)))
        self.assertFalse(Point(5, 5).is_side(Point(4, 4)))
