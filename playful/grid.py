"""
Functions and classes related to a Grid - an organized collection of Points.
"""
from typing import Set

from playful.point import Point


class Grid:
    """A Grid is an organized collection of Points."""

    def __init__(self, points: Set[Point]) -> None:
        self.points = set(points)

    @classmethod
    def create(cls, width: int, height: int) -> "Grid":
        """Return a new Grid instance with a given width and height."""
        points = {Point(x, y) for x in range(width) for y in range(height)}
        return cls(points)

    def __eq__(self, other: "Grid") -> bool:
        """Return a boolean indicating whether two grid objects are equal."""
        return isinstance(other, Grid) and (self.points == other.points)
