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
