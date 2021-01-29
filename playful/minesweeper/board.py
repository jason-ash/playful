"""Minesweeper Board class"""
from collections import Counter
from typing import Dict, NamedTuple, Set

from playful.minesweeper.cell import Cell


class Board(NamedTuple):
    """A minesweeper Board contains a set of Cells and methods to play the game."""

    cells: Set[Cell]

    def __repr__(self) -> str:
        """Return a string representation of this Board."""
        attributes = dict(
            height=self.height,
            width=self.width,
            bombs=self.bombs,
            **self.states(),
        )
        attrs = ", ".join(f"{k}={repr(v)}" for k, v in attributes.items())
        return f"{self.__class__.__qualname__}({attrs})"

    @property
    def bombs(self) -> int:
        """Return the number of bombs contained in this Board."""
        return sum(cell.is_bomb() for cell in self.cells)

    @property
    def height(self) -> int:
        """Return the height (y) dimension of this Board."""
        return max(cell.location.y for cell in self.cells) + 1

    @property
    def width(self) -> int:
        """Return the width (x) dimension of this Board."""
        return max(cell.location.x for cell in self.cells) + 1

    def states(self) -> Dict[str, int]:
        """Return a dictionary of the states of all Cells in this Board."""
        return Counter(cell.state for cell in self.cells)

    def bomb_cells(self) -> Set["Cell"]:
        """Return the set of Cells in this Board that contain bombs."""
        return set(cell for cell in self.cells if cell.is_bomb())

    def safe_cells(self) -> Set["Cell"]:
        """Return the set of Cells in this Board that don't contain bombs."""
        return set(cell for cell in self.cells if not cell.is_bomb())

    def flagged_cells(self) -> Set["Cell"]:
        """Return the set of Cells in this Board that have been flagged."""
        return set(cell for cell in self.cells if cell.state == "flagged")

    def hidden_cells(self) -> Set["Cell"]:
        """Return the set of Cells in this Board that have been hidden."""
        return set(cell for cell in self.cells if cell.state == "hidden")

    def revealed_cells(self) -> Set["Cell"]:
        """Return the set of Cells in this Board that have been revealed."""
        return set(cell for cell in self.cells if cell.state == "revealed")
