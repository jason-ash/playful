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
            ("match", "match", ("m", "a", "t", "c", "h")),
            ("tacos", "tails", ("t", "a", "", "", "s")),
            ("misos", "mosso", ("m", "", "s", "", "")),
            ("misos", "sassy", ("", "", "s", "", "")),
            ("sorts", "funds", ("", "", "", "", "s")),
            ("tangy", "zzzzz", ("", "", "", "", "")),
            ("crazy", "jazzy", ("", "", "", "z", "y")),
        ]
        for secret, guess, output in cases:
            with self.subTest(f"testing secret='{secret}' with guess='{guess}'"):
                self.assertEqual(correct_letters(secret=secret, guess=guess), output)

    def test_excluded_letters(self):
        """Test identifying single or multiple letters that we know aren't included."""
        cases = [
            ("match", "match", ()),
            ("tangy", "zzzzz", ("z",)),
            ("misos", "sumps", ("p", "u")),
            ("misos", "mosso", ("oo",)),
            ("misos", "sassy", ("a", "sss", "y")),
            ("robed", "worry", ("rr", "w", "y")),
            ("crazy", "jazzy", ("j", "zz")),
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
            ("crazy", "jazzy", ("", "a", "", "", "")),
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
        for word, letters, output in cases:
            with self.subTest(f"testing word='{word}' with letters='{letters}'"):
                self.assertEqual(has_correct_letters(word, letters), output)

    def test_has_excluded_letters(self):
        """Test identifying candidate words that contain excluded letters"""
        cases = [
            ("river", ("r",), True),
            ("river", ("rr",), True),
            ("river", ("rrr",), False),
            ("abbot", ("t",), True),
            ("abbot", ("b",), True),
            ("abbot", ("bb",), True),
            ("abbot", ("bbb",), False),
        ]
        for word, letters, output in cases:
            with self.subTest(f"testing word='{word}' with letters='{letters}'"):
                self.assertEqual(has_excluded_letters(word, letters), output)

    def test_has_misplaced_letters(self):
        """Test identifying candidate words that contain misplaced letters"""
        cases = [
            ("river", ("", "", "", "r", ""), True),
            ("river", ("", "", "", "", "r"), False),
            ("river", ("r", "", "", "", ""), False),
            ("river", ("", "r", "r", "", ""), True),
            ("river", ("r", "", "", "", "r"), False),
            ("abbot", ("b", "", "", "b", ""), True),
            ("abbot", ("b", "b", "", "", ""), False),
            ("abbot", ("", "a", "", "", ""), True),
            ("abbot", ("a", "", "", "", ""), False),
        ]
        for word, letters, output in cases:
            with self.subTest(f"testing word='{word}' with letters='{letters}'"):
                self.assertEqual(has_misplaced_letters(word, letters), output)

    def test_is_potential_solution(self):
        """Test identifying words that are still potential solutions"""
        cases = [
            ("match", "match", "match", True),
            ("match", "match", "other", False),
            ("robed", "worry", "robed", True),
            ("robed", "worry", "river", False),
        ]
        for secret, guess, word, output in cases:
            with self.subTest():
                self.assertEqual(is_potential_solution(secret, guess, word), output)
