"""
Functions to play the word guessing game from the Lingo game show
https://en.wikipedia.org/wiki/Lingo_(American_game_show)
"""
from typing import Tuple


def correct_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return a tuple of letters where the guess letter equals the secret letter."""
    return tuple(t if t == g else "" for t, g in zip(secret, guess))


def excluded_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return letters that we know aren't included in the secret word."""
    return ("",)


def misplaced_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return a tuple identifying letters that are in the secret word, but misplaced."""


def has_correct_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word contains all correct letters."""
    return all(x == y if y else True for x, y in zip(word, letters))


def has_excluded_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word contains any excluded letters."""


def has_misplaced_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word matches the misplaced letters."""


def is_potential_solution(secret: str, guess: str, word: str) -> bool:
    """Return if a candidate word could be a solution to a secret word, given a guess."""
    # 1. ensure the candidate word has all the letters we already know about.
    if not has_correct_letters(word, correct_letters(secret=secret, guess=guess)):
        return False

    # 2. ensure the word doesn't have any letters we know shouldn't be included.
    if has_excluded_letters(word, excluded_letters(secret=secret, guess=guess)):
        return False

    # 3. ensure the word has known, but misplaced, letters.
    if not has_misplaced_letters(word, misplaced_letters(secret=secret, guess=guess)):
        return False

    return True
