"""
Functions to play the word guessing game from the Lingo game show
https://en.wikipedia.org/wiki/Lingo_(American_game_show)
"""
from typing import Iterable, List, Tuple


def correct_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return a tuple of letters where the guess letter equals the secret letter."""
    return tuple(t if t == g else "" for t, g in zip(secret, guess))


def excluded_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return letters that we know aren't included in the secret word."""
    excluded = []
    for letter in set(guess):
        occurrences = secret.count(letter)
        if occurrences == 0:
            excluded.append(letter)
        else:
            if guess.count(letter) > occurrences:
                excluded.append(letter * (occurrences + 1))
    return tuple(sorted(excluded))


def misplaced_letters(secret: str, guess: str) -> Tuple[str, ...]:
    """Return a tuple identifying letters that are in the secret word, but misplaced."""
    available = [s for s, g in zip(secret, guess) if s != g]
    misplaced = []
    for secret_letter, guess_letter in zip(secret, guess):
        if secret_letter != guess_letter and guess_letter in available:
            misplaced.append(guess_letter)
            available.remove(guess_letter)
        else:
            misplaced.append("")
    return tuple(misplaced)


def has_correct_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word contains all correct letters."""
    return all(x == y if y else True for x, y in zip(word, letters))


def has_excluded_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word contains any excluded letters."""
    return any(word.count(letter[0]) >= len(letter) for letter in letters)


def has_misplaced_letters(word: str, letters: Tuple[str, ...]) -> bool:
    """Return a boolean indicating if a candidate word matches the misplaced letters."""
    has_letters = all(letter in word for letter in letters)
    has_positions = all(w != letter for w, letter in zip(word, letters))
    return has_letters and has_positions


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


def potential_solutions(secret: str, guess: str, words: Iterable[str]) -> List[str]:
    """Return a list of words that are still potential solutions, given a guess."""
    return [
        w for w in words if is_potential_solution(secret=secret, guess=guess, word=w)
    ]


def partitions(guess: str, words: Iterable[str]) -> List[List[str]]:
    """Return a list of the partitions that a guess will create among a list of words."""
    wordset = set(words)
    out = []
    while wordset:
        word = sorted(wordset)[0]
        partition = set(potential_solutions(secret=word, guess=guess, words=wordset))
        out.append(sorted(partition))
        wordset = wordset - set(partition)
    return out


def best_splitting_word(candidates: Iterable[str], words: Iterable[str]) -> str:
    """Return the word that splits a partition of words into the most sub-partitions."""
    best_word, best_split = "", 0
    for word in candidates:
        partition = partitions(guess=word, words=words)
        if len(partition) > best_split:
            best_word, best_split = word, len(partition)
    return best_word
