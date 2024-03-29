"""Test point.py"""
import unittest

from playful.core import Point


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

    def test_reflect_x(self):
        """Test reflecting a point over a vertical line"""
        point = Point(4, 4)
        x_value = 7
        reflection = Point(10, 4)
        self.assertEqual(point.reflect(x=x_value), reflection)

    def test_reflect_y(self):
        """Test reflecting a point over a horizontal line"""
        point = Point(4, 4)
        y_value = 1
        reflection = Point(4, -2)
        self.assertEqual(point.reflect(y=y_value), reflection)

    def test_reflect_xy(self):
        """Test reflecting a point over a horizontal and vertical lines"""
        point = Point(4, 4)
        x_value, y_value = 7, 1
        reflection = Point(10, -2)
        self.assertEqual(point.reflect(x=x_value, y=y_value), reflection)

    def test_reflect_identity(self):
        """Test reflecting a point over itself"""
        point = Point(4, 4)
        x_value, y_value = 4, 4
        reflection = Point(4, 4)
        self.assertEqual(point.reflect(x=x_value, y=y_value), reflection)

    def test_rotate_identity(self):
        """Test rotating a point around itself"""
        point = Point(4, 4)
        around = Point(4, 4)
        rotation = Point(4, 4)
        self.assertEqual(point.rotate(around=around, degrees=0), rotation)
        self.assertEqual(point.rotate(around=around, degrees=90), rotation)
        self.assertEqual(point.rotate(around=around, degrees=180), rotation)
        self.assertEqual(point.rotate(around=around, degrees=270), rotation)

    def test_rotate_raises(self):
        """Test raising an error for rotation degrees not multiple of 90"""
        point = Point(4, 4)
        around = Point(5, 5)
        self.assertRaises(ValueError, point.rotate, around, 120)

    def test_rotate(self):
        """Test some sample rotations"""
        point = Point(8, 10)
        around = Point(7, 7)
        self.assertEqual(point.rotate(around=around, degrees=90), Point(10, 6))
        self.assertEqual(point.rotate(around=around, degrees=180), Point(6, 4))
        self.assertEqual(point.rotate(around=around, degrees=270), Point(4, 8))
        self.assertEqual(point.rotate(around=around, degrees=-90), Point(4, 8))
