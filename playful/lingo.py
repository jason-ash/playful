"""
Functions to play the word guessing game from the Lingo game show
https://en.wikipedia.org/wiki/Lingo_(American_game_show)
"""
from typing import Optional, Tuple


def correct_letters(secret: str, guess: Optional[str] = None) -> Tuple[str, ...]:
    """
    Return a tuple identifying which letters in the secret word were correctly guessed.

    Examples
    --------
    >>> correct_letters("tacos")
    ('', '', '', '', '')
    >>> correct_letters("tacos", "tails")
    ('t', 'a', '', '', 's')
    >>> correct_letters("misos", "mosso")
    ('m', '', 's', '', '')
    >>> correct_letters("misos", "sassy")
    ('', '', 's', '', '')
    """
    if guess is None:
        return tuple("" for _ in secret)
    return tuple(t if t == g else "" for t, g in zip(secret, guess))


def misplaced_letters(secret: str, guess: Optional[str] = None) -> Tuple[str, ...]:
    """
    Return a tuple identifying letters that are in the secret word, but misplaced.

    Examples
    --------
    >>> misplaced_letters("tacos")
    ('', '', '', '', '')
    >>> misplaced_letters("tacos", "teach")
    ('', '', 'a', 'c', '')
    >>> misplaced_letters("misos", "sumps")
    ('s', '', 'm', '', '')
    >>> misplaced_letters("misos", "mosso")
    ('', 'o', '', 's', '')
    >>> misplaced_letters("misos", "sassy")
    ('s', '', '', '', '')
    """
    if guess is None:
        return tuple("" for _ in secret)

    # before identifying misplaced letters, we need to account for correct letters.
    # we only want to flag letters in the secret word that aren't in the correct spot.
    correct = correct_letters(secret=secret, guess=guess)
    available = [s for s, c in zip(secret, correct) if c == ""]

    misplaced = []
    for secret_letter, guess_letter in zip(secret, guess):
        if secret_letter != guess_letter and guess_letter in available:
            misplaced.append(guess_letter )
            available.remove(guess_letter)
        else:
            misplaced.append("")
    return tuple(misplaced)
