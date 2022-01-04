"""Minesweeper Cell class"""
from collections import Counter
from typing import Dict, Iterable, NamedTuple, Set

from playful.core import Point


class Cell(NamedTuple):
    """
    A Cell in minesweeper is one of the spaces on the board.

    Each Cell is identified with x and y coordinates, stored as a Point instance, a
    value, which ranges from -1 to 8, and a state, which can be one of "hidden",
    "revealed", or "flagged". The Cell's value remains constant, but Cell states will
    change as the game is played. Cells are immutable, so a Cell's state is changed by
    replacing the original Cell with a new Cell.

    Parameters
    ----------
    location : Point, a container for the Cell's xy coordinates, plus useful methods
    value : int, a number between -1 and 8, where -1 is used to indicate a bomb, and
        the numbers 0 through 8 are used to identify how many bombs a Cell touches
    state : str, an indicator for the Cell's state, which can be "flagged", "hidden",
        or "revealed"
    """

    location: Point
    value: int
    state: str

    def is_bomb(self) -> bool:
        """Return a boolean indicating whether this cell contains a bomb or not."""
        return self.value == -1

    def neighbors(self, cells: Iterable["Cell"]) -> Set["Cell"]:
        """Return a set of the Cells among a group that border this Cell."""
        # we have to pass an iterable of Cells to this function because a Cell has no
        # concept of its neighbors - that only exists in the context of a Board object.
        return set(cell for cell in cells if cell.location in self.location.borders())

    def neighbor_states(self, cells: Iterable["Cell"]) -> Dict[str, int]:
        """Return a dictionary of the states and counts of this Cell's neighbors."""
        return Counter(cell.state for cell in self.neighbors(cells))
