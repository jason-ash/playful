"""
Functions to play the word guessing game from the Lingo game show
https://en.wikipedia.org/wiki/Lingo_(American_game_show)
"""
from typing import Tuple


# typing alias for a tuple of single letters
Letters = Tuple[str, ...]


def correct_letters(secret: str, guess: str) -> Letters:
    """
    Return a tuple identifying which letters in the secret word were correctly guessed.

    Examples
    --------
    >>> correct_letters("tacos", "tails")
    ('t', 'a', '', '', 's')
    >>> correct_letters("misos", "mosso")
    ('m', '', 's', '', '')
    >>> correct_letters("misos", "sassy")
    ('', '', 's', '', '')
    """
    return tuple(t if t == g else "" for t, g in zip(secret, guess))


def misplaced_letters(secret: str, guess: str) -> Letters:
    """
    Return a tuple identifying letters that are in the secret word, but misplaced.

    Examples
    --------
    >>> misplaced_letters("tacos", "teach")
    ('', '', 'a', 'c', '')
    >>> misplaced_letters("misos", "sumps")
    ('s', '', 'm', '', '')
    >>> misplaced_letters("misos", "mosso")
    ('', 'o', '', 's', '')
    >>> misplaced_letters("misos", "sassy")
    ('s', '', '', '', '')
    """
    # before identifying misplaced letters, we need to account for correct letters.
    # we only want to flag letters in the secret word that aren't in the correct spot.
    correct = correct_letters(secret=secret, guess=guess)
    available = [s for s, c in zip(secret, correct) if c == ""]

    misplaced = []
    for secret_letter, guess_letter in zip(secret, guess):
        if secret_letter != guess_letter and guess_letter in available:
            misplaced.append(guess_letter)
            available.remove(guess_letter)
        else:
            misplaced.append("")
    return tuple(misplaced)


def incorrect_letters(secret: str, guess: str) -> Letters:
    """
    Return a tuple identifying letters that were guess that are not in the secret word.

    Examples
    --------
    >>> incorrect_letters("tangy", "zzzzz")
    ('z', 'z', 'z', 'z', 'z')
    >>> incorrect_letters("tacos", "tails")
    ('', '', 'i', 'l', '')
    >>> incorrect_letters("misos", "mosso")
    ('', '', '', '', 'o')
    >>> incorrect_letters("misos", "sassy")
    ('', 'a', '', 's', 'y')
    >>> incorrect_letters()
    """
    correct = correct_letters(secret=secret, guess=guess)
    misplaced = misplaced_letters(secret=secret, guess=guess)
    return tuple(
        g if g != s and c == "" and m == "" else ""
        for s, g, c, m in zip(secret, guess, correct, misplaced)
    )
