"""
Functions and classes related to Points.

At the most basic level, a Point is an (x, y) pair of coordinates that defines a
location. Usually this corresponds to a location on a game board, but the concept is
abstract enough that it could generalize beyond a literal location if necessary.
"""
from typing import NamedTuple, Set


class Point(NamedTuple):
    """
    A Point is a location identified by x and y coordinates.

    A Point implements methods to understand its surroundings and to generate new
    Points, for example by rotating around another point or reflecting over an axis.
    """

    x: int
    y: int

    def borders(self) -> Set["Point"]:
        """Return a set of Points surrounding this Point in all directions."""
        return self.corners().union(self.sides())

    def corners(self) -> Set["Point"]:
        """Return a set of the corners surrounding this Point."""
        return {
            Point(x=self.x + 1, y=self.y + 1),
            Point(x=self.x - 1, y=self.y + 1),
            Point(x=self.x - 1, y=self.y - 1),
            Point(x=self.x + 1, y=self.y - 1),
        }

    def sides(self) -> Set["Point"]:
        """Return a set of the sides surrounding this Point."""
        return {
            Point(x=self.x + 1, y=self.y),
            Point(x=self.x - 1, y=self.y),
            Point(x=self.x, y=self.y + 1),
            Point(x=self.x, y=self.y - 1),
        }
