"""Minesweeper Board class"""
from collections import Counter
from itertools import product
import random
from typing import Dict, NamedTuple, Optional, Set

from playful.core import Point
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

    @classmethod
    def create(
        cls, height: int, width: int, n_bombs: int, random_state: Optional[int]
    ) -> "Board":
        """Create a Board with a given size and number of randomly-distributed bombs."""
        random.seed(random_state)
        points = [Point(x, y) for x, y in product(range(height), range(width))]
        bombs = set(random.sample(points, n_bombs))
        cells = {
            Cell(
                p,
                value=-1 if p in bombs else len(p.borders().intersection(bombs)),
                state="hidden",
            )
            for p in points
        }
        return cls(cells)

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
        return Counter(sorted(cell.state for cell in self.cells))

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
