"""Test playful/lingo.py"""
import unittest

from playful.lingo import (
    correct_letters,
    excluded_letters,
    misplaced_letters,
    has_correct_letters,
    has_excluded_letters,
    has_misplaced_letters,
    is_potential_solution,
)


class TestLingo(unittest.TestCase):
    """Test Lingo functions"""

    def test_correct_letters(self):
        """Test identifying correct letters, given a secret word and a guess"""
        cases = [
            ("tacos", "tails", ("t", "a", "", "", "s")),
            ("misos", "mosso", ("m", "", "s", "", "")),
            ("misos", "sassy", ("", "", "s", "", "")),
            ("sorts", "funds", ("", "", "", "", "s")),
            ("tangy", "zzzzz", ("", "", "", "", "")),
        ]
        for secret, guess, output in cases:
            with self.subTest(f"testing secret='{secret}' with guess='{guess}'"):
                self.assertEqual(correct_letters(secret=secret, guess=guess), output)

    def test_excluded_letters(self):
        """Test identifying single or multiple letters that we know aren't included."""
        cases = [
            ("match", "match", ("",)),
            ("tangy", "zzzzz", ("z",)),
            ("misos", "sumps", ("p", "u")),
            ("misos", "mosso", ("oo",)),
            ("misos", "sassy", ("a", "sss", "y")),
            ("robed", "worry", ("rr", "w", "y")),
        ]
        for secret, guess, output in cases:
            with self.subTest(f"testing secret='{secret}' with guess='{guess}'"):
                self.assertEqual(excluded_letters(secret=secret, guess=guess), output)

    def test_misplaced_letters(self):
        """Test identifying misplaced letters, given a secret word and a guess"""
        cases = [
            ("tacos", "teach", ("", "", "a", "c", "")),
            ("misos", "sumps", ("s", "", "m", "", "")),
            ("misos", "mosso", ("", "o", "", "s", "")),
            ("misos", "sassy", ("s", "", "", "", "")),
            ("robed", "worry", ("", "", "r", "", "")),
        ]
        for secret, guess, output in cases:
            with self.subTest(f"testing secret='{secret}' with guess='{guess}'"):
                self.assertEqual(misplaced_letters(secret=secret, guess=guess), output)

    def test_has_correct_letters(self):
        """Test identifying candidate words that contain all correct letters"""
        cases = [
            ("river", ("r", "", "", "", ""), True),
            ("river", ("r", "", "", "", "r"), True),
            ("river", ("r", "", "r", "", "r"), False),
            ("abbot", ("", "b", "", "", ""), True),
            ("abbot", ("b", "", "", "", ""), False),
            ("abbot", ("a", "b", "b", "o", "t"), True),
        ]
        for candidate, exclusions, output in cases:
            with self.subTest():
                self.assertEqual(has_correct_letters(candidate, exclusions), output)

    def test_has_excluded_letters(self):
        """Test identifying candidate words that contain excluded letters"""
        cases = [
            ("river", ("r",), True),
            ("river", ("rr",), True),
            ("river", ("rrr",), True),
            ("abbot", ("t",), True),
            ("abbot", ("b",), True),
            ("abbot", ("bb",), True),
            ("abbot", ("bbb",), False),
        ]
        for candidate, exclusions, output in cases:
            with self.subTest():
                self.assertEqual(has_excluded_letters(candidate, exclusions), output)

    def test_has_misplaced_letters(self):
        """Test identifying candidate words that contain misplaced letters"""
        cases = [
            ("river", ("r",), True),
            ("river", ("rr",), True),
            ("river", ("rrr",), True),
            ("abbot", ("t",), True),
            ("abbot", ("b",), True),
            ("abbot", ("bb",), True),
            ("abbot", ("bbb",), False),
        ]
        for candidate, exclusions, output in cases:
            with self.subTest():
                self.assertEqual(has_misplaced_letters(candidate, exclusions), output)

    def test_is_potential_solution(self):
        """Test identifying words that are still potential solutions"""
        cases = [
            ("robed", "worry", "river", False),  # ruled out because of second 'r'
        ]
        for secret, guess, word, output in cases:
            with self.subTest():
                self.assertEqual(is_potential_solution(secret, guess, word), output)
