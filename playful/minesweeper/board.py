"""Minesweeper Board class"""
from collections import Counter
from itertools import product
import random
import typing
from typing import NamedTuple, Optional, Set

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
        cls, width: int, height: int, n_bombs: int, random_state: Optional[int] = None
    ) -> "Board":
        """Create a Board with a given size and number of randomly-distributed bombs."""
        random.seed(random_state)
        points = [Point(x, y) for x, y in product(range(width), range(height))]
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

    def visualize(self) -> str:
        """Return a string visualization of the Board and its cells."""
        border = f"#{'-' * (self.width * 2 - 1)}#"
        contents = "\n"
        for row in range(self.height):
            cells = sorted(c for c in self.cells if c.location.y == row)
            contents += "|" + "|".join(c.visualize() for c in cells) + "|\n"
        return border + contents + border

    def _get_cell(self, location: Point) -> Optional[Cell]:
        """Return the Cell on this Board at a given location."""
        return next((c for c in self.cells if c.location == location), None)

    def _change_cell_state(self, location: Point, state: str) -> "Board":
        """Return a new Board after updating the state of one of its cells."""
        # if a cell doesn't exist at that location, just return the current set of cells.
        cell = self._get_cell(location=location)
        if cell:
            cells = (self.cells - {cell}).union({cell.change_state(state=state)})
        else:
            cells = self.cells
        return self.__class__(cells)

    def flag(self, location: Point) -> "Board":
        """Return a new Board after flagging the Cell at a given location."""
        # make sure we don't flag a revealed cell
        cell = self._get_cell(location=location)
        if cell is None or cell.state == "revealed":
            return self
        return self._change_cell_state(location=location, state="flagged")

    def reveal(self, location: Point) -> "Board":
        """
        Return a new Board after revealing the Cell at a given location.

        If the revealed Cell has a value of 0 (no neighboring bombs), then we want to
        recursively reveal all neighboring Cells until the last Cells we have revealed
        contain numbers. We reveal all Cells, even if they have been flagged, as this
        is only likely to reveal Cells that were flagged incorrectly anyway.

        If there is no Cell at the given location, return the original Board.
        """
        cell = self._get_cell(location=location)
        if cell is None or cell.state == "revealed":
            return self

        out = self._change_cell_state(location=location, state="revealed")
        if cell.value != 0:
            return out

        for neighbor in location.borders():
            out = out.reveal(neighbor)
        return out

    def reveal_all(self) -> "Board":
        """Return a new Board with all Cells revealed."""
        return self.__class__({cell.change_state("revealed") for cell in self.cells})

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

    def states(self) -> typing.Counter[str]:
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
