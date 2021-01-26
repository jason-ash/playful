"""
Functions and classes related to Points.

At the most basic level, a Point is an (x, y) pair of coordinates that defines a
location. Usually this corresponds to a location on a game board, but the concept is
abstract enough that it could generalize beyond a literal location if necessary.
"""
from typing import NamedTuple, Optional, Set


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

    def is_border(self, other: "Point") -> bool:
        """Return a boolean indicating if this Point is bordered by another Point."""
        return other in self.borders()

    def is_corner(self, other: "Point") -> bool:
        """Return a boolean indicating if this Point is the corner of another Point."""
        return other in self.corners()

    def is_side(self, other: "Point") -> bool:
        """Return a boolean indicating if this Point is the side of another Point."""
        return other in self.sides()

    # pylint: disable=invalid-name
    def reflect(self, x: Optional[int] = None, y: Optional[int] = None) -> "Point":
        """
        Return a new Point by reflecting over x and/or y lines.

        If x or y is None, then the point won't be reflected over those axes. Therefore,
        the default arguments of this function will return the original Point.

        Parameters
        ----------
        x : Optional[int], default None, the vertical line across which to reflect
        y : Optional[int], default None, the horizontal line across which to refect

        Examples
        --------
        >>> Point(4, 4).reflect(x=6)
        Point(x=8, y=4)
        >>> Point(4, 4).reflect(y=1)
        Point(x=4, y=-2)
        >>> Point(4, 4).reflect(x=6, y=1)
        Point(x=8, y=-2)
        >>> Point(4, 4).reflect()
        Point(x=4, y=4)
        """
        x = x or self.x
        y = y or self.y
        dx = x - self.x
        dy = y - self.y
        return Point(x=x + dx, y=y + dy)

    # pylint: disable=invalid-name
    def rotate(self, around: "Point", degrees: int) -> "Point":
        """
        Return a new Point by rotating around another Point.

        Parameters
        ----------
        around : Point, the point around which to rotate
        degrees : int, the number of degrees to rotate. Must be a multiple of 90.

        Examples
        --------
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=90)
        Point(x=10, y=6)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=180)
        Point(x=6, y=4)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=270)
        Point(x=4, y=8)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=360)
        Point(x=8, y=10)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=-90)
        Point(x=4, y=8)
        >>> Point(5, 5).rotate(around=Point(5, 5), degrees=180)
        Point(x=5, y=5)
        >>> Point(8, 10).rotate(around=Point(x=7, y=7), degrees=120)
        Traceback (most recent call last):
        ...
        ValueError: degrees must be a multiple of 90
        """
        # constrain degrees to 0, 90, 180, 270; otherwise raise an error
        degrees = degrees % 360
        if degrees not in [0, 90, 180, 270]:
            raise ValueError("degrees must be a multiple of 90")

        if degrees == 0:
            return Point(x=self.x, y=self.y)

        # recursively rotate 90 degrees at a time until we reach our goal
        dx, dy = self.x - around.x, self.y - around.y
        x, y = around.x + dy, around.y - dx
        return Point(x=x, y=y).rotate(around=around, degrees=degrees - 90)
